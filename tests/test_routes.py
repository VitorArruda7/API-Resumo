from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_summarize_route():
    response = client.post("/summarize", json={"url": "https://example.com"})
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
    assert "summary" in data