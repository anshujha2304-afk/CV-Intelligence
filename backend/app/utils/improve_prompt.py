IMPROVE_PROMPT = """
You are an expert ATS resume writer.

Improve the resume below.

Return ONLY valid JSON.

The field "overall_rating" MUST be an integer between 0 and 100.

Schema:

{{
    "professional_summary":"",
    "rewritten_bullet_points":[],
    "improved_skills":[],
    "missing_keywords":[],
    "ats_improvements":[],
    "overall_rating":0
}}

Resume:

{resume}
"""