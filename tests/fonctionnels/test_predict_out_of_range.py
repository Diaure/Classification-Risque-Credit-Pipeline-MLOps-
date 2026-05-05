# Demander à l'API de renvoyer une réponse 200 lorsqu'on a un age du type -5 ou un revenu à '0'
from fastapi.testclient import TestClient
from App.main import app
from App.models import ClientFeatures

def test_out_of_range_values():
    client = TestClient(app)

    example = ClientFeatures.model_config["json_schema_extra"]["example"].copy()

    # Cas 1 : âge impossible
    if "DAYS_BIRTH" in example:
        example["DAYS_BIRTH"] = -5

    # Cas 2 : revenu impossible
    if "AMT_INCOME_TOTAL" in example:
        example["AMT_INCOME_TOTAL"] = 0

    response = client.post("/predict", json=example)

    # L'API ne doit pas planter
    assert response.status_code == 200

    data = response.json()
    assert "score" in data
    assert "decision" in data
