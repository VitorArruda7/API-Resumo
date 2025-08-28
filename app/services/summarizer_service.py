from app.core.config import settings

# Tentativa de usar Hugging Face
try:
    from transformers import pipeline
    import torch

    summarizer = pipeline("summarization", model=settings.MODEL_NAME)
    USE_HF_MODEL = True
except Exception:
    summarizer = None
    USE_HF_MODEL = False

def summarize_text(text: str, max_length: int = 130, min_length: int = 30) -> str:
    """
    Resume um texto usando o modelo definido na env MODEL_NAME.
    Se houver algum problema com PyTorch ou Hugging Face, faz um resumo simplificado.
    """
    if USE_HF_MODEL and summarizer:
        try:
            summary = summarizer(
                text,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )
            return summary[0]["summary_text"]
        except Exception:
            # Caso falhe o uso do modelo
            pass

    # Fallback: pega os primeiros 500 caracteres e junta parágrafos
    paragraphs = text.split("\n")
    content = " ".join(paragraphs)
    fallback_summary = content[:500] + "..." if len(content) > 500 else content
    return fallback_summary