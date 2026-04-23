import os
import json
import re
from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_keywords(domain: str, audience: str):
 
    prompt = f"""
You are an SEO expert.

Business Info:
Company Website: {domain}
Target Audience: {audience}

Understand what this company likely does based on its name/domain.
Then generate keywords relevant to its business and audience.

Generate 10 HIGH-INTENT SEO search queries that:

- reflect real Google searches
- include specific use cases
- include modifiers like "best", "for", "near me", "pricing", etc.
- are relevant to BOTH the domain and audience

Avoid generic queries.

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