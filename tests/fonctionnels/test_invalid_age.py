from fastapi.testclient import TestClient
from App.main import app
from tests.utils import TEST_EXAMPLE

def test_invalid_age():
    client = TestClient(app)
    example = TEST_EXAMPLE.copy()

    example["DAYS_BIRTH"] = -5  # âge impossible

    response = client.post("/predict", json=example)

    assert response.status_code == 422
    assert "Âge invalide" in response.json()["detail"]
