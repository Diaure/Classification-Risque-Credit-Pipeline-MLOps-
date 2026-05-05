from fastapi import FastAPI
import joblib
import pandas as pd
from models import ClientFeatures

app = FastAPI()

# Charger le pipeline (préprocessing + modèle)
pipe = joblib.load("./BestModel/pipeline_complet.joblib")

# Charger le seuil optimal
threshold = joblib.load("./BestModel/best_threshold.joblib")

# Validation métier
df = joblib.load("./data/app_test_clean_v2.joblib")
if "DAYS_BIRTH" in df.columns:
    if df["DAYS_BIRTH"].iloc[0] > -18*365 or df["DAYS_BIRTH"].iloc[0] >= 0:
        raise HTTPException(status_code=422, detail="Âge invalide pour un dossier crédit.")

if "AMT_INCOME_TOTAL" in df.columns:
    if df["AMT_INCOME_TOTAL"].iloc[0] <= 0:
        raise HTTPException(status_code=422, detail="Revenu invalide pour un dossier crédit.")


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
