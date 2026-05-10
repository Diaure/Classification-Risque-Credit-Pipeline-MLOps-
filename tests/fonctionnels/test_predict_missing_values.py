# Notre modèle accepte les NaN, donc il faut tester que l'API accepte les valeurs manquantes

from fastapi.testclient import TestClient
from App.main import app
from App.models import ClientFeatures

def test_missing_values_in_columns():
    client = TestClient(app)
    example = ClientFeatures.model_config["json_schema_extra"]["example"].copy()

    # Remplace 5 colonnes par None
    for k in list(example.keys())[:5]:
        example[k] = None

    response = client.post("/predict", json=example)

    assert response.status_code == 200

