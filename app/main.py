from fastapi import FastAPI
from app import routes

app = FastAPI(title="Article Summarizer API", version="1.0.0")

app.include_router(routes.router)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Article Summarizer API running"}