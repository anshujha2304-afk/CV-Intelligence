from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.resume import router as resume_router

app = FastAPI(
    title="CV-Intelligence API",
    version="1.0.0",
    description="AI-powered Resume Analysis Platform",
)

app.include_router(auth_router)
app.include_router(resume_router)


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Welcome to CV-Intelligence API 🚀",
    }