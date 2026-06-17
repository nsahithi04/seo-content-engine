import os
import json
import re
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_outline(keyword: str, serp_results: list):

    combined_text = ""

    for r in serp_results:
        combined_text += f"Title: {r.get('title')} \n"
        combined_text += f"Snippet: {r.get('snippet')} \n\n"
        
    prompt = f"""
You are an SEO expert.

Target Keyword:
{keyword}

Top ranking content (from Google):
{combined_text}

Based on this, create a HIGH-QUALITY SEO article outline.

Requirements:
- Include a compelling title
- Include H2 sections
- Include H3 subsections under each H2
- Include FAQs at the end
- Follow patterns seen in top-ranking pages

Return ONLY valid JSON in this format:

{{
  "title": "...",
  "sections": [
    {{
      "heading": "...",
      "subsections": ["...", "..."]
    }}
  ],
  "faqs": ["...", "..."]
}}

No explanation.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    content = response.text

    print(f"\nOUTLINE RAW OUTPUT for [{keyword}]:", content)

    match = re.search(r"\{.*\}", content, re.DOTALL)

    if match:
        try:
            data = json.loads(match.group())
            return data
        except Exception as e:
            print("OUTLINE JSON ERROR:", e)
            return {}
    else:
        print("NO OUTLINE JSON FOUND")
        return {}