from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.schemas.analysis import ResumeAnalysis


class UploadResponse(BaseModel):
    filename: str
    characters: int
    name: str
    email: str
    phone: str
    linkedin: str | None = None
    github: str | None = None
    skills: list[str]
    preview: str
    ats_score: int
    strengths: list[str]
    improvements: list[str]
    ai_feedback: str
    ai_analysis: ResumeAnalysis


class ResumeHistoryItem(BaseModel):
    id: UUID
    filename: str
    name: str | None = None
    email: str | None = None
    ats_score: int
    created_at: datetime


class ResumeHistoryResponse(BaseModel):
    resumes: list[ResumeHistoryItem]


class ResumeDetailResponse(BaseModel):
    id: UUID
    filename: str
    characters: int
    name: str
    email: str
    phone: str
    linkedin: str | None = None
    github: str | None = None
    skills: list[str]
    preview: str
    ats_score: int
    strengths: list[str]
    improvements: list[str]
    ai_feedback: str
    ai_analysis: ResumeAnalysis
    created_at: datetime