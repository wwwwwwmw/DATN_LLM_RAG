"""
LLM RAG Service — FastAPI Application
Local LLM Pipeline (no third-party API keys needed)
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes import router as api_router

app = FastAPI(
    title="MedTech LLM RAG",
    description="Medical Consultation RAG Pipeline with local LLM",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")


@app.get("/")
def root():
    return {
        "service": "llm-rag",
        "version": "1.0.0",
        "embedding_model": settings.EMBEDDING_MODEL,
        "llm_model": settings.LLM_MODEL,
    }


@app.get("/health")
def health():
    return {"status": "ok", "models_loaded": settings.MODELS_LOADED}
