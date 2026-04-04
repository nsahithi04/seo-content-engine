from fastapi import FastAPI
from app.routes.keyword_routes import router as keyword_router

app = FastAPI()

app.include_router(keyword_router)