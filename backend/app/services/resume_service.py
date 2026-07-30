from fastapi import HTTPException, UploadFile

from app.core.logger import logger

from app.services.parser import extract_pdf, extract_docx
from app.services.extractor import (
    extract_name,
    extract_email,
    extract_phone,
    extract_links,
    extract_skills,
)
from app.services.ats import calculate_ats_score
from app.services.ai_feedback import (
    analyze_resume_ai,
    generate_feedback,
)
from app.services.resume_repository import save_resume


def process_resume(file: UploadFile, user_id: str):
    logger.info(f"Resume upload request received: {file.filename}")

    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        text = extract_pdf(file)

    elif filename.endswith(".docx"):
        text = extract_docx(file)

    else:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported."
        )

    logger.info(f"Successfully parsed {file.filename}")

    ai_analysis = analyze_resume_ai(text)

    logger.info("AI analysis completed.")

    linkedin, github = extract_links(text)

    data = {
        "filename": file.filename,
        "characters": len(text),
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "linkedin": linkedin,
        "github": github,
        "skills": extract_skills(text),
        "resume_text": text,
        "preview": text[:500],
    }

    data.update(calculate_ats_score(data))

    logger.info(f"ATS Score: {data['ats_score']}")

    data["ai_feedback"] = generate_feedback(data)
    data["ai_analysis"] = ai_analysis

    saved = save_resume(user_id, data)

    logger.info("Resume saved successfully.")

    response = saved.copy()
    response.pop("resume_text", None)

    return response