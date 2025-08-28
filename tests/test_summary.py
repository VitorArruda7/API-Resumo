from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_summarize_with_text():
    payload = {
        "text": "Python é uma linguagem de programação popular, criada por Guido van Rossum em 1991. "
                "Ela é conhecida por sua simplicidade e legibilidade."
    }
    response = client.post("/summary/summarize", json=payload)
    assert response.status_code == 200
    assert "summary" in response.json()

def test_summarize_without_input():
    response = client.post("/summary/summarize", json={})
    assert response.status_code == 400
    assert response.json()["detail"] == "Texto ou URL são obrigatórios"
