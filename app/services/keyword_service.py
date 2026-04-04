import os
import json
import re
from dotenv import load_dotenv
from google import genai

# load env
load_dotenv()

# create client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_keywords(domain: str, audience: str):
    prompt = f"""
You are an SEO expert.

Given:
- Company domain: {domain}
- Target audience: {audience}

Generate 10 high-intent Google search queries.

Return ONLY valid JSON in this format:

{{
  "keywords": [
    "keyword 1",
    "keyword 2"
  ]
}}

No explanation.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    content = response.text

    print("RAW LLM OUTPUT:", content)

    # extract JSON safely
    match = re.search(r"\{.*\}", content, re.DOTALL)

    if match:
        try:
            data = json.loads(match.group())
            return data.get("keywords", [])
        except Exception as e:
            print("JSON ERROR:", e)
            return []
    else:
        print("NO JSON FOUND")
        return []