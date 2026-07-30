import json

from app.core.ai_client import client, MODEL
from app.utils.prompts import RESUME_ANALYSIS_PROMPT


def generate_feedback(data):

    prompt = f"""
You are an expert ATS recruiter.

Analyze the following resume.

Name:
{data["name"]}

ATS Score:
{data["ats_score"]}

Skills:
{", ".join(data["skills"])}

Strengths:
{", ".join(data["strengths"])}

Improvements:
{", ".join(data["improvements"])}

Write your response in Markdown using these headings:

# Overall Review
# Strengths
# Weaknesses
# ATS Improvement Tips
# Interview Advice

Keep the response professional and concise.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
    )

    return response.choices[0].message.content


def analyze_resume_ai(resume_text):

    prompt = RESUME_ANALYSIS_PROMPT.format(
        text=resume_text
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
    )

    content = response.choices[0].message.content.strip()

    # Remove markdown code blocks if the model returns them
    content = (
        content
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        return json.loads(content)

    except json.JSONDecodeError:

        return {
            "error": "Model returned invalid JSON",
            "raw_response": content
        }