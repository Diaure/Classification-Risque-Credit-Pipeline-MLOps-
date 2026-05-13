import gradio as gr
import joblib
import pandas as pd
from models import ClientFeatures
import sys, os
import re

# ROOT = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(ROOT)

# Charger le pipeline
pipe = joblib.load("./BestModel/pipeline_complet.joblib")

# Charger le seuil optimal
threshold = joblib.load("./BestModel/best_threshold.joblib")

# Récupérer l'exemple généré automatiquement dans models.py
example = ClientFeatures.model_config["json_schema_extra"]["example"]

def sanitize(name: str) -> str:
    """
    Transforme un nom de colonne en identifiant Python valide.
    """
    # Remplacer tout caractère non alphanumérique par un underscore
    name = re.sub(r'[^0-9a-zA-Z_]', '_', name)

    # Si le nom commence par un chiffre → préfixer
    if re.match(r'^[0-9]', name):
        name = f"col_{name}"

    return name

def predict_gradio(*args):
    try:
        # Reconstruction automatique
        data_dict = {name: value for (name, value) in zip(ClientFeatures.model_fields.keys(), args)}
        df = pd.DataFrame([data_dict])
        df.columns = [sanitize(c) for c in df.columns]

        # Conversion robuste : transforme tout ce qui peut être un nombre
        df = df.apply(lambda col: pd.to_numeric(col, errors="coerce"))

        # Validation métier
        if "DAYS_BIRTH" in df.columns:
            raw_age = df["DAYS_BIRTH"].iloc[0]

            # Forcer la conversion en float de manière robuste
            try:
                age = float(raw_age)
            except (TypeError, ValueError):
                age = None

            # Si on a bien un nombre, on applique la règle métier
            if age is not None and (age >= 0 or age > -18 * 365):
                return "Âge invalide", None, None
            

        if "AMT_INCOME_TOTAL" in df.columns:
            income = df["AMT_INCOME_TOTAL"].iloc[0]
            if pd.notna(income) and income <= 0:
                return "Revenu invalide", None, None

        # Prédiction
        score = pipe.predict_proba(df)[0][1]
        decision = "ACCORDÉ" if score < threshold else "REFUSÉ"

        return decision, float(score), float(threshold)

    except Exception as e:
        return f"ERREUR : {str(e)}", None, None



# Génération automatique des inputs Gradio AVEC VALEURS PAR DÉFAUT
inputs = []
for name, field in ClientFeatures.model_fields.items():

    default_value = example.get(name, None)

    if field.annotation == float:
        inputs.append(gr.Number(label=name, value=default_value))
    elif field.annotation == int:
        inputs.append(gr.Number(label=name, value=default_value))
    elif field.annotation == bool:
        inputs.append(gr.Checkbox(label=name, value=default_value))
    elif field.annotation == str:
        inputs.append(gr.Textbox(label=name, value=default_value))
    else:
        inputs.append(gr.Textbox(label=name, value=default_value))


# Sorties Gradio
outputs = [
    gr.Textbox(label="Décision"),
    gr.Number(label="Score"),
    gr.Number(label="Seuil Optimal"),
]

# Interface Gradio
app = gr.Interface(
    fn=predict_gradio,
    inputs=inputs,
    outputs=outputs,
    title="Scoring Crédit - Interface Gradio",
    description="Interface interactive pour tester le modèle de scoring crédit."
)

app.launch()
