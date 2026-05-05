# Générer un example de donnée pour un client
import pandas as pd
import json
import joblib
import numpy as np

df = joblib.load("./data/app_test_clean_v2.joblib")

# Prendre un individu au hasard
example = df.sample(1).iloc[0].to_dict()
for k, v in example.items():
    if isinstance(v, float) and (np.isnan(v)):
        example[k] = None



# Afficher sous format JSON
print(json.dumps(example, indent=4))
