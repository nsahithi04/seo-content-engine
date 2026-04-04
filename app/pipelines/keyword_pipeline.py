from app.services.keyword_service import generate_keywords
from app.services.serp_service import fetch_serp_results


def run_keyword_pipeline(domain: str, audience: str):
    keywords = generate_keywords(domain, audience)

    enriched_keywords = []

    print("KEYWORDS:", keywords)

    for kw in keywords[:5]:
        serp_data = fetch_serp_results(kw) 

        enriched_keywords.append({
            "keyword": kw,
            "serp_results": serp_data
        })

    return {
        "data": enriched_keywords
    }