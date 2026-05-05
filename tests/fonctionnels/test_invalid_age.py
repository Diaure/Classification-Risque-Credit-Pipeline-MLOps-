from fastapi.testclient import TestClient
from App.main import app
from App.models import ClientFeatures

def test_invalid_age():
    client = TestClient(app)
    example = ClientFeatures.model_config["json_schema_extra"]["example"].copy()

    example["DAYS_BIRTH"] = -5  # âge impossible

    response = client.post("/predict", json=example)

    assert response.status_code == 422
    assert "Âge invalide" in response.json()["detail"]
