from fastapi.testclient import TestClient
from App.main import app
from tests.utils import TEST_EXAMPLE

def test_invalid_income():
    client = TestClient(app)
    example = TEST_EXAMPLE.copy()

    example["AMT_INCOME_TOTAL"] = 0  # revenu impossible

    response = client.post("/predict", json=example)

    assert response.status_code == 422
    assert "Revenu invalide" in response.json()["detail"]
