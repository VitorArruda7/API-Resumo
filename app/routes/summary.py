from fastapi import APIRouter, HTTPException
from typing import Optional
from app.models.summary import SummarizeRequest, SummarizeResponse
from app.services.scraper_service import fetch_article_text
from app.services.summarizer_service import summarize_text
from app.core.config import settings

router = APIRouter()

@router.post("/summarize", response_model=SummarizeResponse)
def summarize_article(request: SummarizeRequest):
    """
    Recebe uma URL ou um texto para gerar um resumo.
    Se nenhum for fornecido, retorna 400.
    """
    try:
        if not request.url and not request.text:
            raise HTTPException(status_code=400, detail="É necessário fornecer uma URL ou texto.")

        if request.url:
            text = fetch_article_text(request.url)
        else:
            text = request.text

        summary = summarize_text(text)

        return SummarizeResponse(
            title=f"Resumo gerado com {settings.MODEL_NAME}",
            summary=summary
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
