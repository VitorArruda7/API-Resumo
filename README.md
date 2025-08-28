# 📝 Article Summarizer API

API de **Inteligência Artificial** que resume artigos automaticamente a partir de **URL** ou **texto direto**, usando o modelo de summarization do Hugging Face Transformers.

## 🛠 **Tecnologias Utilizadas**

- Python 3.11
- FastAPI
- Pydantic
- Transformers (Hugging Face)
- BeautifulSoup4
- Docker
- Docker Compose
- Pytest

## 📁 **Estrutura de diretórios**
```bash
├── app/
│   ├── main.py           # Inicialização da API FastAPI
│   ├── routes/
│   │   └── summary.py    # Rota POST /summary/summarize
│   ├── models/
│   │   └── summary.py    # Pydantic models: SummarizeRequest e SummarizeResponse
│   ├── services/
│   │   ├── scraper_service.py    # Função fetch_article_text
│   │   └── summarizer_service.py # Função summarize_text
│   └── core/
│       └── config.py     # Configurações gerais (MODEL_NAME, etc)
├── tests/
│   ├── test_routes.py
│   └── test_summary.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ **Rodando Localmente**

- Criar e ativar o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

- Instalar dependências:
```bash
pip install -r requirements.txt
```

- Rodar a API:
```bash
uvicorn app.main:app --reload
```

- A API ficará disponível em: http://127.0.0.1:8000

---

## 🐳 **Rodando com Docker**

- Build e start do container:
```bash
docker-compose up --build
```

- Acessar a API em: http://localhost:8000

- Para parar o container:
```bash
docker-compose down
```

---

## 🚀 **Endpoints**

- Health Check
```bash
GET /health
```

- Response
```bash
{
  "status": "ok"
}
```

- Summarize Article
```bash
POST /summary/summarize
Content-Type: application/json
```

- Request (URL ou texto)
```bash
{
  "url": "https://exemplo.com/artigo",
  "text": null
}
```
## OU
```bash
{
  "url": null,
  "text": "Texto direto para resumir."
}
```

- Response
```bash
{
  "title": "Resumo gerado com distilbart-cnn-12-6",
  "summary": "Resumo do artigo ou texto aqui."
}
```

---

## 🧪 **Testes**

- Rodar todos os testes com pytest:
```bash
pytest -v
```

---

## 🔧 **Configurações**
No arquivo .env você pode definir variáveis de configuração (opcional):
```bash
MODEL_NAME=distilbart-cnn-12-6
```