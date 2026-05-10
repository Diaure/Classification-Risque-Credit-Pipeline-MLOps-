# Vérifier que les prédictions sont valides
from fastapi.testclient import TestClient
from App.main import app
from App.models import ClientFeatures

def test_predict_valid():
    client = TestClient(app)
    example = ClientFeatures.model_config["json_schema_extra"]["example"]

    response = client.post("/predict", json=example)
    assert response.status_code == 200

    data = response.json()
    assert "score" in data
    assert "decision" in data
    assert "threshold" in data
