from fastapi import FastAPI
from app.routes.summary import router

app = FastAPI(title="Article Summarizer API", version="1.0.0")

app.include_router(router, prefix="/summary", tags=["Summary"])

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Article Summarizer API running"}