from fastapi import APIRouter

router = APIRouter()

from fastapi import APIRouter
from app.models.summarize import SummarizeRequest, SummarizeResponse

router = APIRouter()

@router.post("/summarize", response_model=SummarizeResponse)
def summarize_article(request: SummarizeRequest):
    # 🚧 Mock inicial - depois substituímos pela lógica real
    return SummarizeResponse(
        title="Mock Title",
        summary=f"Summary for article at {request.url}"
    )
