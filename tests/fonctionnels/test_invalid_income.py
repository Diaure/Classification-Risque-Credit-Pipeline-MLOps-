from fastapi.testclient import TestClient
from App.main import app
from App.models import ClientFeatures

def test_invalid_income():
    client = TestClient(app)
    example = ClientFeatures.model_config["json_schema_extra"]["example"].copy()

    example["AMT_INCOME_TOTAL"] = 0  # revenu impossible

    response = client.post("/predict", json=example)

    assert response.status_code == 422
    assert "Revenu invalide" in response.json()["detail"]
