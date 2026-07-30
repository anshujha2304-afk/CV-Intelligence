from pydantic import BaseModel, Field


class Education(BaseModel):
    degree: str = ""
    institution: str = ""
    year: str = ""


class Experience(BaseModel):
    company: str = ""
    role: str = ""
    duration: str = ""


class Project(BaseModel):
    title: str = ""
    description: str = ""
    technologies: list[str] = Field(default_factory=list)


class Certification(BaseModel):
    name: str = ""
    topics: list[str] = Field(default_factory=list)


class ResumeAnalysis(BaseModel):
    skills: list[str] = Field(default_factory=list)

    education: list[Education] = Field(default_factory=list)

    experience: list[Experience] = Field(default_factory=list)

    projects: list[Project] = Field(default_factory=list)

    certifications: list[Certification] = Field(default_factory=list)

    strengths: list[str] = Field(default_factory=list)

    weaknesses: list[str] = Field(default_factory=list)