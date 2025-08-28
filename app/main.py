# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# ---------------------
# ROTA DE HEALTHCHECK
# ---------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# ---------------------
# MODEL PARA REQUISIÇÃO DE RESUMO
# ---------------------
class SummaryRequest(BaseModel):
    text: Optional[str] = None
    url: Optional[str] = None

# ---------------------
# ROTA DE SUMMARIZE
# ---------------------
@app.post("/summary/summarize")
def summarize(req: SummaryRequest):
    if not req.text and not req.url:
        raise HTTPException(status_code=400, detail="Texto ou URL são obrigatórios")
    
    # Substitua esta parte pela sua lógica de resumo real
    summary_result = ""
    if req.text:
        # Exemplo simples de resumo: pegar as primeiras 100 caracteres
        summary_result = req.text[:100]
    elif req.url:
        # Aqui você pode colocar a lógica de scraping + resumo
        summary_result = f"Resumo do conteúdo de {req.url}"
    
    return {"summary": summary_result}
