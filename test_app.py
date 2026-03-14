from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["message"] == "Hello from CI/CD!"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_item():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json()["item_id"] == 42
    assert response.json()["name"] == "Item number 42"
