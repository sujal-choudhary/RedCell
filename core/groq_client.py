import os
import socket
from groq import Groq


# Initialize Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)


def ask_ai(prompt: str) -> str:
    if not os.environ.get("GROQ_API_KEY"):
        return "[AI ERROR] GROQ_API_KEY not set"

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are RedCell AI. "
                        "Answer in VERY SHORT form. "
                        "Use bullet points only. "
                        "Maximum 4 bullets. "
                        "No examples, no stories."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.1,
            max_tokens=120
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"[AI ERROR] {str(e)}"
