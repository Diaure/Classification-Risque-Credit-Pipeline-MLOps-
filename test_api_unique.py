import requests
import pandas as pd
import numpy as np
import joblib

API_URL = "http://localhost:8000/predict"

# Charger dataset de référence
df_example = joblib.load("./data/app_test_clean_v2.joblib")

# Détection des colonnes booléennes (0/1)
bool_cols = [col for col in df_example.columns if set(df_example[col].dropna().unique()).issubset({0, 1})]

sent_payloads = set()

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

def generate_unique_input(df):
    while True:
        idx = np.random.randint(0, len(df))
        payload = df.iloc[idx].to_dict()
        key = tuple(sorted(payload.items()))
        if key not in sent_payloads:
            sent_payloads.add(key)
            return sanitize_payload(payload)


# Envoi des requêtes
def send_requests(n=200):
    for i in range(n):
        payload = generate_unique_input(df_example)
        # payload = sanitize_payload(payload)

        response = requests.post(API_URL, json=payload)

        print(f"{i+1}/{n} → {response.status_code}")
        if response.status_code != 200:
            print("Erreur API :", response.text)
    print("\nRequêtes uniques envoyées :", len(sent_payloads))

def send_requests(n=200):
    for i in range(n):
        payload = generate_unique_input(df_example)
        response = requests.post(API_URL, json=payload)
        print(f"{i+1}/{n} → {response.status_code}")
        if response.status_code != 200:
            print("Erreur API :", response.text)

    print("\nRequêtes uniques envoyées :", len(sent_payloads))

# Lancer le test
if __name__ == "__main__":
    send_requests(200)

