import re


def extract_job_skills(description: str):
    skill_database = [
        "python",
        "java",
        "c",
        "c++",
        "javascript",
        "typescript",
        "react",
        "node",
        "fastapi",
        "django",
        "flask",
        "sql",
        "postgresql",
        "mongodb",
        "git",
        "docker",
        "kubernetes",
        "aws",
        "azure",
        "gcp",
        "linux",
        "tensorflow",
        "pytorch",
        "opencv",
        "machine learning",
        "deep learning",
        "html",
        "css"
    ]

    description = description.lower()

    found = []

    for skill in skill_database:
        if re.search(r"\b" + re.escape(skill) + r"\b", description):
            found.append(skill)

    return found


def match_resume(resume_data, job_description):

    resume_skills = {
        skill.lower()
        for skill in resume_data.get("skills", [])
    }

    job_skills = set(extract_job_skills(job_description))

    matched = sorted(resume_skills & job_skills)

    missing = sorted(job_skills - resume_skills)

    if len(job_skills) == 0:
        score = 0
    else:
        score = round(len(matched) / len(job_skills) * 100)

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }