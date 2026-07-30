import json

from app.core.ai_client import client, MODEL
from app.utils.improve_prompt import IMPROVE_PROMPT


def improve_resume(resume_text):

    prompt = IMPROVE_PROMPT.format(
        resume=resume_text
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    content = response.choices[0].message.content.strip()

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
            "error": "Invalid JSON returned by AI",
            "raw_response": content
        }