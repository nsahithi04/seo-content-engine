from pydantic import BaseModel
from typing import List


class KeywordRequest(BaseModel):
    domain: str
    audience: str


class KeywordResponse(BaseModel):
    keywords: List[str]