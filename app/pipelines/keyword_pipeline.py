from app.services.keyword_service import generate_keywords
from app.services.serp_service import fetch_serp_results
from app.services.outline_service import generate_outline
from app.services.content_service import generate_article
from app.services.draft_service import save_draft


def run_keyword_pipeline(domain: str, audience: str):
    keywords = generate_keywords(domain, audience)

    enriched_keywords = []

    print("KEYWORDS:", keywords)

    for kw in keywords[:1]:
        serp_data = fetch_serp_results(kw) 

        outline = generate_outline(kw, serp_data)

        article = generate_article(kw,outline)

        save_draft(kw,article)

        enriched_keywords.append({
        "keyword": kw,
        "serp_results": serp_data,
        "outline": outline,
        "article": article
    })


    return {
        "data": enriched_keywords
    }