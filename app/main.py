from fastapi import FastAPI
from app.config import settings
from app.api.v1.endpoints import router as api_router

app = FastAPI(
    title=settings.app_title,
    version=settings.app_version,
    description="FastAPI application refactored with uv for JKN Cybersecurity & DLP RAG Pipeline and Literature Gap Matrix."
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/", summary="Root Endpoint")
def read_root():
    return {
        "message": "Welcome to JKN Cybersecurity & DLP RAG Pipeline API",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
        "api_v1_base": "/api/v1"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
