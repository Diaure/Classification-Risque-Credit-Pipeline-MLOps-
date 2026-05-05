# Vérifier que l'API démarre réellement
from fastapi.testclient import TestClient
from App.main import app

def test_api_starts():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code in [200, 404]
