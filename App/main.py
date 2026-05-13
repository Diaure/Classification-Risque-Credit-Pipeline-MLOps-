# 
from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi
import joblib
import pandas as pd
import json
from App.models import ClientFeatures

app = FastAPI()
@app.get("/")
def root():
    return {"status": "ok"}

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

# Exemple dynamique dans Swagger (/docs)
# Charger dataset une seule fois
try:
    df_example = joblib.load("./data/app_test_clean_v2.joblib")
except:
    df_example = None  # sécurité si le fichier n'existe pas dans l'environnement

def generate_random_example():
    if df_example is None:
        return {}
    row = df_example.sample(1).iloc[0].to_dict()
    # Remplacer NaN par None pour Swagger
    for k, v in row.items():
        if isinstance(v, float) and pd.isna(v):
            row[k] = None
    return row

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    schema = get_openapi(
        title="Home Credit API",
        version="1.0",
        routes=app.routes,)

    # Injecter l'exemple dynamique dans le schéma OpenAPI
    try:
        schema["components"]["schemas"]["ClientFeatures"]["example"] = generate_random_example()
    except KeyError:
        pass  # sécurité si le schéma n'est pas encore généré

    app.openapi_schema = schema
    return schema

app.openapi = custom_openapi
