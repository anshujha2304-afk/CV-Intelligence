def calculate_ats_score(data):

    score = 0
    strengths = []
    improvements = []

    # Contact Information
    if data.get("email"):
        score += 10
        strengths.append("Email found")
    else:
        improvements.append("Add an email address")

    if data.get("phone"):
        score += 10
        strengths.append("Phone number found")
    else:
        improvements.append("Add a phone number")

    # Links
    if data.get("linkedin"):
        score += 10
        strengths.append("LinkedIn profile found")
    else:
        improvements.append("Add your LinkedIn profile")

    if data.get("github"):
        score += 10
        strengths.append("GitHub profile found")
    else:
        improvements.append("Add your GitHub profile")

    # Skills
    skill_count = len(data.get("skills", []))

    if skill_count >= 10:
        score += 30
        strengths.append("Excellent technical skill coverage")

    elif skill_count >= 5:
        score += 20
        strengths.append("Good technical skills")

    elif skill_count > 0:
        score += 10
        strengths.append("Some technical skills detected")

    else:
        improvements.append("Add a dedicated Skills section")

    # Resume Length
    chars = data.get("characters", 0)

    if chars >= 1500:
        score += 20
        strengths.append("Good resume length")
    else:
        improvements.append("Resume appears too short")

    # Name
    if data.get("name"):
        score += 10
        strengths.append("Name detected")

    return {
        "ats_score": min(score, 100),
        "strengths": strengths,
        "improvements": improvements
    }