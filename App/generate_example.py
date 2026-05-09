# Générer un example de donnée pour un client
import pandas as pd
import json
import joblib
import numpy as np
from typing import Optional

df = joblib.load("./data/app_test_clean_v2.joblib")

# Prendre un individu au hasard
example = df.sample(1).iloc[0].to_dict()
for k, v in example.items():
    if isinstance(v, float) and (np.isnan(v)):
        example[k] = None

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

# Afficher sous format JSON
print(json.dumps(example, indent=4))
