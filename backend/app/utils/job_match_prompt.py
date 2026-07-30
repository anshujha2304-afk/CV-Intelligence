JOB_MATCH_PROMPT = """
You are an expert technical recruiter.

Compare the following resume and job description.

Return ONLY valid JSON.

Schema:

{{
    "overall_match": 0,
    "technical_match": 0,
    "experience_match": 0,
    "matched_skills": [],
    "missing_skills": [],
    "strengths": [],
    "weaknesses": [],
    "resume_improvements": [],
    "learning_recommendations": [],
    "summary": ""
}}

Resume:

{resume}

Job Description:

{job_description}
"""