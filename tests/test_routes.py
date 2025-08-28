from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_summary_route_real():
    url = "https://pt.wikipedia.org/wiki/Python"
    response = client.post("/summary/summarize", json={"url": url})
    assert response.status_code == 200
    assert "summary" in response.json()