from pydantic import BaseModel
from typing import Optional

class SummarizeRequest(BaseModel):
    url: Optional[str] = None
    text: Optional[str] = None

class SummarizeResponse(BaseModel):
    title: str
    summary: str
