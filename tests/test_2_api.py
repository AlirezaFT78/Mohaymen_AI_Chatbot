from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ask_endpoint():
    response = client.post("/ask", json={"query": "تو چی هستی؟"})
    assert response.status_code == 200
    assert "مهیمن" in response.json()["answer"]
