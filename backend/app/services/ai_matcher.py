import os
import json

from dotenv import load_dotenv
from groq import Groq

from app.utils.job_match_prompt import JOB_MATCH_PROMPT

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ai_match_resume(resume_text: str, job_description: str):
    prompt = JOB_MATCH_PROMPT.format(
        resume=resume_text,
        job_description=job_description
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
    )

    content = response.choices[0].message.content.strip()

    # Remove markdown if present
    content = (
        content
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        result = json.loads(content)

        # Normalize score fields
        score_fields = [
            "overall_match",
            "technical_match",
            "experience_match"
        ]

        for field in score_fields:
            value = result.get(field)

            if value is None:
                result[field] = 0
                continue

            # Convert decimal scores (0.82 -> 82)
            if isinstance(value, float):
                if 0 <= value <= 1:
                    result[field] = int(round(value * 100))
                else:
                    result[field] = int(round(value))

            elif isinstance(value, int):
                result[field] = value

            elif isinstance(value, str):
                try:
                    number = float(value)

                    if 0 <= number <= 1:
                        result[field] = int(round(number * 100))
                    else:
                        result[field] = int(round(number))

                except ValueError:
                    result[field] = 0

            else:
                result[field] = 0

        return result

    except json.JSONDecodeError:
        raise ValueError(
            f"AI returned invalid JSON:\n\n{content}"
        )