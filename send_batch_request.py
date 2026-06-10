import requests
import pandas as pd
import numpy as np
import joblib

API_URL = "http://localhost:8000/predict"

# Charger dataset de référence
df_example = joblib.load("./data/app_test_clean_v2.joblib")

# Détection des colonnes booléennes (0/1)
bool_cols = [col for col in df_example.columns if set(df_example[col].dropna().unique()).issubset({0, 1})]

# sent_payloads = set()

def sanitize_payload(payload):
    clean = {}
    for k, v in payload.items():
        if pd.isna(v):
            clean[k] = None
        elif isinstance(v, (np.integer, np.int64)):
            clean[k] = int(v)
        elif isinstance(v, (np.floating, np.float64)):
            clean[k] = float(v)
        else:
            clean[k] = v
    return clean

df_aleatoire = df_example.sample(frac = 1, random_state = 42).reset_index(drop = True)
batch_size = 200
n_batch = 10

for i in range(n_batch):
    df_batch = df_aleatoire.iloc[i * batch_size: (i + 1) * batch_size]
    payload = [sanitize_payload(row) for row in df_batch.to_dict(orient="records")]
    response = requests.post("http://localhost:8000/predict_batch", json=payload)
    print(f"Batch {i+1} envoyé")

# Lancer le test
# send_requests(200)
print("Status:", response.status_code)
print(response.json())
