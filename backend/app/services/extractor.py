import re
from app.utils.skills import SKILLS


def extract_email(text):
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return match.group() if match else None


def extract_phone(text):
    match = re.search(r"(\+?\d[\d\s-]{8,}\d)", text)
    return match.group() if match else None


def extract_links(text):
    linkedin = None
    github = None

    for line in text.splitlines():
        lower = line.lower()

        if "linkedin.com" in lower:
            linkedin = line.strip()

        if "github.com" in lower:
            github = line.strip()

    return linkedin, github


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(set(found_skills))


def extract_name(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return lines[0] if lines else None