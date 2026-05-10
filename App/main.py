# 
from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
import json
from App.models import ClientFeatures

app = FastAPI()

# Charger le pipeline MLflow (attend les colonnes ORIGINALES)
pipe = joblib.load("./BestModel/pipeline_complet.joblib")

# Charger le seuil optimal
threshold = joblib.load("./BestModel/best_threshold.joblib")

# Charger le mapping clean -> original
with open("App/column_mapping.json") as f:
    COLUMN_MAPPING = json.load(f)


@app.post("/predict")
def predict(features: ClientFeatures):

    # Validation métier
    data = features.dict()

    # Âge invalide
    if "DAYS_BIRTH" in data and data["DAYS_BIRTH"] is not None:
        # Test attend : âge impossible → 422 + "Âge invalide"
        if data["DAYS_BIRTH"] > 0 or data["DAYS_BIRTH"] > -18*365:
            raise HTTPException(
                status_code=422,
                detail="Âge invalide")

    # Revenu invalide
    if "AMT_INCOME_TOTAL" in data and data["AMT_INCOME_TOTAL"] is not None:
        if data["AMT_INCOME_TOTAL"] <= 0:
            raise HTTPException(
                status_code=422,
                detail="Revenu invalide")

    # Conversion en DataFrame
    df = pd.DataFrame([data])

    # Remapping clean à l'original
    df = df.rename(columns=COLUMN_MAPPING)

    # Vérifier que toutes les colonnes attendues par MLflow sont présentes
    missing = set(pipe.feature_names_in_) - set(df.columns)
    if missing:
        raise HTTPException(
            status_code=422,
            detail=f"Colonnes manquantes après remapping : {missing}")

    # Prédiction MLflow
    score = pipe.predict_proba(df)[0][1]
    decision = "ACCORDÉ" if score < threshold else "REFUSÉ"

    return {
        "score": float(score),
        "decision": decision,
        "threshold": float(threshold)
    }
