from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from App.models import ClientFeatures

app = FastAPI()

# Charger le pipeline
pipe = joblib.load("./BestModel/pipeline_complet.joblib")

# Charger le seuil optimal
threshold = joblib.load("./BestModel/best_threshold.joblib")


@app.post("/predict")
def predict(data: ClientFeatures):

    # Convertir les données brutes en DataFrame
    df = pd.DataFrame([data.model_dump()])   # model_dump = Pydantic v2

    # Âge impossible
    if "DAYS_BIRTH" in df.columns:
        age = df["DAYS_BIRTH"].iloc[0]
        if age >= 0 or age > -18 * 365:
            raise HTTPException(
                status_code=422,
                detail="Âge invalide pour un dossier crédit."
            )

    # Revenu impossible
    if "AMT_INCOME_TOTAL" in df.columns:
        income = df["AMT_INCOME_TOTAL"].iloc[0]
        if income <= 0:
            raise HTTPException(
                status_code=422,
                detail="Revenu invalide pour un dossier crédit."
            )

    score = pipe.predict_proba(df)[0][1]
    decision = "ACCORDÉ" if score < threshold else "REFUSÉ"

    return {
        "score": float(score),
        "decision": decision,
        "threshold": float(threshold)
    }
