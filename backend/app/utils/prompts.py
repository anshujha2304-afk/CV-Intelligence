RESUME_ANALYSIS_PROMPT = """
You are an expert ATS resume analyzer.

Analyze the resume below.

Return ONLY valid JSON.

Schema:

{{
    "skills": [],
    "projects": [],
    "education": [],
    "experience": [],
    "certifications": [],
    "strengths": [],
    "weaknesses": [],
    "overall_score": 0,
    "summary": ""
}}

Resume:

{text}
"""