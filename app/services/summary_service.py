import requests
from bs4 import BeautifulSoup

def summarize_url(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return f"Erro ao acessar a URL: {e}"

    soup = BeautifulSoup(response.text, "html.parser")

    # Captura parágrafos do texto
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]

    if not paragraphs:
        return "Não foi possível encontrar conteúdo relevante para resumir."

    # Junta os parágrafos e pega só os 3 primeiros para resumir
    content = " ".join(paragraphs[:5])

    # Aqui está um resumo bem simples
    summary = content[:500] + "..." if len(content) > 500 else content

    return summary