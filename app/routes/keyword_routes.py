from fastapi import APIRouter
from app.schemas.keyword_schema import KeywordRequest
from app.controllers.keyword_controller import handle_generate_keywords

router = APIRouter()

@router.post("/keywords")
def generate_keywords(data: KeywordRequest):
    return handle_generate_keywords(data)