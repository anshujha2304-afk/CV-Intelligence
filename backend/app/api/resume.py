from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.dependencies.auth import get_current_user
from app.core.logger import logger

from app.schemas.resume import (
    UploadResponse,
    ResumeHistoryResponse,
    ResumeDetailResponse,
)
from app.schemas.match import JobDescription, MatchResponse
from app.schemas.improve import ImproveResponse

from app.services.resume_service import process_resume
from app.services.resume_repository import (
    get_latest_resume,
    get_resume_by_id,
    list_resumes,
    delete_resume,
)
from app.services.ai_matcher import ai_match_resume
from app.services.resume_improver import improve_resume


router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)


# -----------------------------
# Upload Resume
# -----------------------------
@router.post(
    "/upload",
    response_model=UploadResponse,
    summary="Upload and analyze a resume",
    description="""
Upload a PDF or DOCX resume.

The API extracts resume information,
calculates an ATS score,
performs AI analysis,
generates recruiter feedback,
and stores the resume in the database.
""",
)
async def upload_resume(
    file: UploadFile = File(...),
    current_user=Depends(get_current_user),
):
    return process_resume(
        file,
        current_user.id,
    )

# -----------------------------
# Resume History
# -----------------------------
@router.get(
    "/history",
    response_model=ResumeHistoryResponse,
    summary="Get resume upload history",
    description="""
Retrieve all uploaded resumes ordered from newest to oldest.
Useful for displaying resume history on the dashboard.
""",
)
async def resume_history(
    current_user=Depends(get_current_user),
):

    logger.info("Fetching resume history.")

    resumes = list_resumes(current_user.id)

    return {
        "resumes": resumes
    }


# -----------------------------
# Get Resume By ID
# -----------------------------
@router.get(
    "/{resume_id}",
    response_model=ResumeDetailResponse,
    summary="Get resume by ID",
    description="Retrieve a specific uploaded resume.",
)
async def get_resume(
    resume_id: str,
    current_user=Depends(get_current_user),
):

    logger.info(f"Fetching resume {resume_id}")

    resume = get_resume_by_id(
    current_user.id,
    resume_id,
)

    if resume is None:
        logger.warning(f"Resume {resume_id} not found.")

        raise HTTPException(
            status_code=404,
            detail="Resume not found.",
        )

    return resume


# -----------------------------
# Delete Resume
# -----------------------------
@router.delete(
    "/{resume_id}",
    summary="Delete a resume",
    description="Delete a resume permanently from the database.",
)
async def remove_resume(
    resume_id: str,
    current_user=Depends(get_current_user),
):
    logger.info(f"Deleting resume {resume_id}")

    resume = get_resume_by_id(
    current_user.id,
    resume_id,
)

    if resume is None:
        logger.warning(f"Resume {resume_id} not found.")

        raise HTTPException(
            status_code=404,
            detail="Resume not found.",
        )

    delete_resume(
    current_user.id,
    resume_id,
)

    logger.info("Resume deleted successfully.")

    return {
        "message": "Resume deleted successfully."
    }


# -----------------------------
# Match Resume
# -----------------------------
@router.post(
    "/match",
    response_model=MatchResponse,
    summary="Match resume with a job description",
    description="""
Compare the uploaded resume with a job description
using AI and return a detailed compatibility report.
""",
)
async def match_job(
    job: JobDescription,
    current_user=Depends(get_current_user),
):

    logger.info("Job matching started.")

    resume = get_latest_resume(current_user.id)

    if resume is None:
        logger.warning("Job matching attempted without uploading a resume.")

        raise HTTPException(
            status_code=404,
            detail="Please upload a resume first.",
        )

    result = ai_match_resume(
        resume.get("resume_text", ""),
        job.description,
    )

    logger.info("Job matching completed.")

    return result


# -----------------------------
# Improve Resume
# -----------------------------
@router.post(
    "/improve",
    response_model=ImproveResponse,
    summary="Improve uploaded resume",
    description="""
Generate ATS-friendly improvements,
rewrite bullet points,
suggest missing keywords,
and provide an improved resume rating.
""",
)
async def improve(
    current_user=Depends(get_current_user),
):

    logger.info("Resume improvement started.")

    resume = get_latest_resume(current_user.id)

    if resume is None:
        logger.warning("Resume improvement attempted without uploading a resume.")

        raise HTTPException(
            status_code=404,
            detail="Please upload a resume first.",
        )

    result = improve_resume(
        resume.get("resume_text", "")
    )

    logger.info("Resume improvement completed.")

    return result