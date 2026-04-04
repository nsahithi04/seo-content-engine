import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERP_API_KEY = os.getenv("SERP_API_KEY")


def fetch_serp_results(keyword: str):
    url = "https://serpapi.com/search"

    params = {
        "q": keyword,
        "api_key": SERP_API_KEY,
        "engine": "google"
    }

    response = requests.get(url, params=params)
    data = response.json()

    results = []

    for item in data.get("organic_results", [])[:5]:
        results.append({
            "title": item.get("title"),
            "link": item.get("link"),
            "snippet": item.get("snippet")
        })

    return results