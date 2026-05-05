from fastapi.testclient import TestClient
from App.main import app
from App.models import ClientFeatures


def test_out_of_range_values():
    client = TestClient(app)

    example = ClientFeatures.model_config["json_schema_extra"]["example"].copy()

    # Cas 1 : âge impossible
    example["DAYS_BIRTH"] = -5

    # Cas 2 : revenu impossible
    example["AMT_INCOME_TOTAL"] = 0

    response = client.post("/predict", json=example)

    # L'API doit refuser ces valeurs
    assert response.status_code == 422
