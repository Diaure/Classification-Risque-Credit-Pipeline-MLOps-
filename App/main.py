# 
from fastapi import FastAPI, HTTPException, Request
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import joblib
import pandas as pd
import json
from App.models import ClientFeatures
import time
import uuid
import json
import logging
from logging.handlers import RotatingFileHandler
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.openapi.utils import get_openapi
import psutil

app = FastAPI()
@app.get("/")
def root():
    return {"status": "ok"}

logger = logging.getLogger("prediction_logger") # objet qui va enregistrer tous les logs d'informations, warning, erreurs mais de debug
logger.setLevel(logging.INFO) # les informations standard de fonctionnement d'API(latence, statut, inputs, outputs, erreurs, etc) : INFO(niveau normal de fonctionnement)

handler = RotatingFileHandler( # définit l'endroit où écrire tous les logs
    "logs/predictions_log.jsonl",
    maxBytes=5_000_000, # lorsque le fichier dépasse 5Mo, 
    backupCount=3) # renomme le fichier en gardant uniquement les 3 dernières versions; s'il y a un 4ème, le plus ancien est supprimé <> éviter de saturer le disque

# Configurer la manière dont les logs seront écrits
formatter = logging.Formatter('%(message)s') # les logs écrits doivent être uniquement sous le format "message" <> jsonl sans aucune autre informations supplémentaires
handler.setFormatter(formatter) # applique le format definit ci-dessus et écrit dans le fichier
logger.addHandler(handler) # connecte le logger au fichier sans quoi rien ne sera écrit
# le format jsonl # json: json est un bloc chargé entièrement en memoire mais difficile pour ajouter de nouvelles données sans reécrire tout le fichier; jsonl (json lines)
# qui écrit un évènement par ligne sous format json, possibilité d'y ajouter autant de ligne sans modifier les reste et sans recharger tout le fichier

# Logs des erreurs 422
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    request_id = getattr(request.state, "request_id", str(uuid.uuid4()))
    log_entry = {
        "request_id": request_id,
        "timestamp": time.time(),
        "path": request.url.path,
        "method": request.method,
        "status": "error",
        "error_message": "ValidationError: " + str(exc.errors()),
        "latency_ms": None,
        "request_size_bytes": int(request.headers.get("content-length", 0)),
        "response_size_bytes": None,
        "cpu_percent": psutil.cpu_percent(),
        "ram_percent": psutil.virtual_memory().percent,
        "system_load": psutil.getloadavg()[0],
        "num_threads": psutil.Process().num_threads()}
    logger.info(json.dumps(log_entry))

    return JSONResponse(
        status_code = 422,
        content={"detail": exc.errors()})

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc):
    request_id = getattr(request.state, "request_id", str(uuid.uuid4()))
    log_entry = {
        "request_id": request_id,
        "timestamp": time.time(),
        "path": request.url.path,
        "method": request.method,
        "status": "error",
        "error_message": f"HTTPException {exc.status_code}: {exc.detail}",
        "latency_ms": None,
        "request_size_bytes": int(request.headers.get("content-length", 0)),
        "response_size_bytes": None,
        "cpu_percent": psutil.cpu_percent(),
        "ram_percent": psutil.virtual_memory().percent,
        "system_load": psutil.getloadavg()[0],
        "num_threads": psutil.Process().num_threads()}
    logger.info(json.dumps(log_entry))

    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail})

# Log de chaque requête
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time() # heure de début pour calculer la latence (delai de réponse entre l'envoi de requete et la réponse retournée)
    request_id = str(uuid.uuid4()) # généré un id pour chaque requete effectuée
    request.state.request_id = request_id
    request_size = int(request.headers.get("content-length", 0)) # Taille de la requête

    try:
        response = await call_next(request) # exécute la requete et si tout fonctionne renvoie "succès"
        status = "success"
        error_message = None
    except Exception as e: # si çà plante, on récupère l'erreur, la loggues, puis renvoie un message à l'utilisateur
        status = "error"
        error_message = str(e)
        response = JSONResponse(
            status_code=500, # 500 statut code "côté serveur" # 400 "côté client"
            content={"detail": "Internal server error"})

    latency_ms = (time.time() - start) * 1000 # calcul du temps de traitement en millisecondes (<= 200 <> bon, 200-500 <> acceptable, >= 500 <> bas ou lent)

    # Taille de la réponse
    response_size = 0
    if hasattr(response, "body"):
        response_size = len(response.body)

    log_entry = { # on va enregistrer
        "request_id": request_id, # l'id de la requete
        "timestamp": time.time(), # l'heure 
        "path": request.url.path, # l'endpoint appelé 
        "method": request.method, # la méthode
        "status": status, # le statut (succès/erreur)
        "error_message": error_message, # le message d'erreur
        "latency_ms": latency_ms,
        "request_size_bytes": request_size,
        "response_size_bytes": response_size,
        "cpu_percent": psutil.cpu_percent(),
        "ram_percent": psutil.virtual_memory().percent,
        "system_load": psutil.getloadavg()[0],
        "num_threads": psutil.Process().num_threads()} # la latence

    logger.info(json.dumps(log_entry))
    return response


# Charger le pipeline MLflow (attend les colonnes ORIGINALES)
pipe = joblib.load("./BestModel/pipeline_complet.joblib")

# Charger le seuil optimal
threshold = joblib.load("./BestModel/best_threshold.joblib")

# Charger le mapping clean -> original
with open("App/column_mapping.json") as f:
    COLUMN_MAPPING = json.load(f)


@app.post("/predict")
def predict(features: ClientFeatures, request: Request):
    request_id = request.state.request_id
    
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
    X_monitoring = pipe[:-1].transform(df)
    X_monitoring = pd.DataFrame(X_monitoring,columns=pipe[:-1].get_feature_names_out())
    # df_transformed = pipe[:-1].transform(df)
    # df_transformed.to_dict()

    result =  {
        "score": float(score),
        "decision": decision,
        "threshold": float(threshold)}

    # Log métier
    log_entry = {
        "request_id": request_id,
        "timestamp": time.time(),
        "path": "/predict",
        "inputs": X_monitoring.iloc[0].to_dict(),
        "score": result["score"],
        "decision": result["decision"],
        "threshold": result["threshold"],
        "cpu_percent": psutil.cpu_percent(),
        "ram_percent": psutil.virtual_memory().percent,
        "system_load": psutil.getloadavg()[0],
        "num_threads": psutil.Process().num_threads()}
    
    logger.info(json.dumps(log_entry))

    return result

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
