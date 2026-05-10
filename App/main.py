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

    # -----------------------------
    # 1) VALIDATIONS MÉTIER
    # -----------------------------

    data = features.dict()

    # Exemple : âge négatif
    if "DAYS_BIRTH" in data and data["DAYS_BIRTH"] is not None:
        if data["DAYS_BIRTH"] > 0:
            raise HTTPException(
                status_code=422,
                detail="DAYS_BIRTH doit être négatif (nombre de jours avant la naissance)."
            )

    # Exemple : revenu incohérent
    if "AMT_INCOME_TOTAL" in data and data["AMT_INCOME_TOTAL"] is not None:
        if data["AMT_INCOME_TOTAL"] <= 0:
            raise HTTPException(
                status_code=422,
                detail="AMT_INCOME_TOTAL doit être strictement positif."
            )

    # -----------------------------
    # 2) Conversion en DataFrame
    # -----------------------------

    df = pd.DataFrame([data])

    # -----------------------------
    # 3) Remapping clean -> original
    # -----------------------------

    df = df.rename(columns=COLUMN_MAPPING)

    # Vérifier que toutes les colonnes attendues par MLflow sont présentes
    missing = set(pipe.feature_names_in_) - set(df.columns)
    if missing:
        raise HTTPException(
            status_code=422,
            detail=f"Colonnes manquantes après remapping : {missing}"
        )

    # -----------------------------
    # 4) Prédiction MLflow
    # -----------------------------

    score = pipe.predict_proba(df)[0][1]
    decision = "ACCORDÉ" if score < threshold else "REFUSÉ"

    return {
        "Score": float(score),
        "Décision": decision,
        "Seuil Optimal": float(threshold)
    }
