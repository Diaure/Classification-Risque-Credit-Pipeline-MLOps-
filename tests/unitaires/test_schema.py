# Vérifier que le schéma Pydandic est cohérent
from App.models import ClientFeatures

def test_schema_has_fields():
    schema = ClientFeatures.model_json_schema()
    assert "properties" in schema
    assert len(schema["properties"]) > 300   # tu as 328 colonnes

# Vérifierquel'exemple fournit dans la documentation swagger est valide
# def test_example_is_valid():
#     example = ClientFeatures.model_config["json_schema_extra"]["example"]
#     obj = ClientFeatures(**example)
#     assert obj is not None
