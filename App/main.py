from fastapi import FastAPI
import joblib
import pandas as pd
from models import ClientFeatures

app = FastAPI()

# Charger le pipeline (préprocessing + modèle)
pipe = joblib.load("./BestModel/pipeline_complet.joblib")

# Charger le seuil optimal
threshold = joblib.load("./BestModel/best_threshold.joblib")

@app.post("/predict")
def predict(data: ClientFeatures):

    # Convertir les données brutes en DataFrame
    df = pd.DataFrame([data.dict()])

    # Prédiction du score (probabilité)
    score = pipe.predict_proba(df)[0][1]

    # Application du seuil
    decision = "ACCORDÉ" if score < threshold else "REFUSÉ"

    return {
        "Score": float(score),
        "Décision": decision,
        "Seuil Optimal": float(threshold)
    }
