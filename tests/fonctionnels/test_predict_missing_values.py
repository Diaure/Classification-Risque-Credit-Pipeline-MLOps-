from fastapi.testclient import TestClient
from App.main import app
from tests.utils import TEST_EXAMPLE

def test_missing_values_in_columns():
    client = TestClient(app)
    example = TEST_EXAMPLE.copy()

    # Remplace 5 colonnes par None
    for k in list(example.keys())[:5]:
        example[k] = None

    response = client.post("/predict", json=example)

    assert response.status_code == 200

