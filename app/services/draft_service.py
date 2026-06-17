import os
import json


def save_draft(keyword: str, article: dict):

    os.makedirs("storage/drafts", exist_ok=True)

    filename = keyword.lower().replace(" ", "-") + ".json"

    filepath = os.path.join(
        "storage",
        "drafts",
        filename
    )

    draft = {
        "keyword": keyword,
        "title": article.get("title"),
        "status": "draft",
        "content": article.get("content")
    }

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(
            draft,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"DRAFT SAVED: {filepath}")