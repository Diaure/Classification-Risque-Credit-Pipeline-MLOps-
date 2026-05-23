# Vérifier que les prédictions sont valides
from fastapi.testclient import TestClient
from App.main import app
from tests.utils import TEST_EXAMPLE

def test_predict_valid():
    client = TestClient(app)
    example = TEST_EXAMPLE.copy()

    response = client.post("/predict", json=example)
    assert response.status_code == 200

    data = response.json()
    assert "score" in data
    assert "decision" in data
    assert "threshold" in data
