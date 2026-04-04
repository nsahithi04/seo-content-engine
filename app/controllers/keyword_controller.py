from app.schemas.keyword_schema import KeywordRequest
from app.pipelines.keyword_pipeline import run_keyword_pipeline


def handle_generate_keywords(data: KeywordRequest):
    result = run_keyword_pipeline(
        domain=data.domain,
        audience=data.audience
    )

    return result