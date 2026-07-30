from pydantic import BaseModel, Field


class JobDescription(BaseModel):
    description: str


class MatchResponse(BaseModel):

    overall_match: int

    technical_match: int

    experience_match: int

    matched_skills: list[str] = Field(default_factory=list)

    missing_skills: list[str] = Field(default_factory=list)

    strengths: list[str] = Field(default_factory=list)

    weaknesses: list[str] = Field(default_factory=list)

    resume_improvements: list[str] = Field(default_factory=list)

    learning_recommendations: list[str] = Field(default_factory=list)

    summary: str