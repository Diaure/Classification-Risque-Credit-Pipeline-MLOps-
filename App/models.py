# models.py
import pandas as pd
import joblib
from pydantic import BaseModel, create_model
from typing import Optional

# Charger le dataset brut (328 colonnes)
df = joblib.load("./data/app_test_clean_v2.joblib")
example = df.sample(1).iloc[0].to_dict()

fields = {}

# Générer automatiquement les types
for col, dtype in df.dtypes.items():
    if dtype == bool or df[col].dropna().isin([0, 1, True, False]).all():
        fields[col] = (Optional[bool], None)

    elif "int" in str(dtype):
        fields[col] = (Optional[int], None)

    elif "float" in str(dtype):
        fields[col] = (Optional[float], None)
        
    else:
        fields[col] = (Optional[str], None)

# Créer le modèle Pydantic
ClientFeatures = create_model("ClientFeatures", **fields)
ClientFeatures.model_config = {
    "json_schema_extra": {
        "example": example}}