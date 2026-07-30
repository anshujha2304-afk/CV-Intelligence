from pydantic import BaseModel, Field


class ImproveResponse(BaseModel):

    professional_summary: str

    rewritten_bullet_points: list[str] = Field(default_factory=list)

    improved_skills: list[str] = Field(default_factory=list)

    missing_keywords: list[str] = Field(default_factory=list)

    ats_improvements: list[str] = Field(default_factory=list)

    overall_rating: int