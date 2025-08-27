from fastapi import APIRouter
from app.models.summary import SummarizeRequest, SummarizeResponse

router = APIRouter()

@router.post("/", response_model=SummarizeResponse)
def summarize_article(request: SummarizeRequest):
    return SummarizeResponse(
        title="Mock Title",
        summary=f"Summary for article at {request.url}"
    )