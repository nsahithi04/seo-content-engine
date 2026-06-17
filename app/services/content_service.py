import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_article(keyword: str, outline: dict):

    prompt = f"""
You are an expert SEO content writer.

Target Keyword:
{keyword}

Article Outline:
{json.dumps(outline, indent=2)}

Write a detailed blog article.

Requirements:
- Follow the outline exactly
- Use H2 and H3 headings
- Be factual and informative
- Write in a professional tone
- Include an introduction
- Include a conclusion
- Answer the FAQ section
- Do NOT use markdown code blocks

Return the complete article only.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return {
        "title": outline.get("title"),
        "content": response.text
    }