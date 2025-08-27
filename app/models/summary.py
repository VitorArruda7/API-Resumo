from pydantic import BaseModel, HttpUrl

class SummarizeRequest(BaseModel):
    url: HttpUrl

class SummarizeResponse(BaseModel):
    title: str
    summary: str
