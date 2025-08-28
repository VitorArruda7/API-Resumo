import requests
from bs4 import BeautifulSoup

def fetch_article_text(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/135.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return f"Erro ao acessar a URL: {e}"

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]

    if not paragraphs:
        return "Não foi possível encontrar conteúdo relevante para resumir."

    content = " ".join(paragraphs[:10])
    return content
