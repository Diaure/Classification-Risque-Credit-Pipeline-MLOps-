import gradio as gr
import joblib
import pandas as pd
import sys, os
import re


# Charger le pipeline
pipe = joblib.load("./BestModel/pipeline_complet.joblib")
print(pipe)

# Charger le seuil optimal
threshold = joblib.load("./BestModel/best_threshold.joblib")

# Charger les données
df_example = joblib.load("./data/app_test_clean_v2.joblib")

# Récupérer les colonnes attendues par le pipeline
expected_cols = pipe.feature_names_in_
print(pipe.feature_names_in_)

example = df_example.sample(1).iloc[0].to_dict()

# Fonction de prédiction
def predict_gradio(*args):
    try:
        # Reconstruction automatique
        data_dict = dict(zip(expected_cols, args)) 
        df = pd.DataFrame([data_dict])
        df = df[expected_cols]

        print("\n=== DEBUG ===")
        print(df.head())
        print("DF columns:", df.columns.tolist())

        if hasattr(pipe, "feature_names_in_"):
            print(pipe.feature_names_in_)

        if hasattr(pipe.named_steps["preprocess"], "transformers_"):
            print("\n===== PREPROCESS EXPECTED =====")

            for name, transfo, cols in pipe.named_steps["preprocess"].transformers_:
                print(f"\nTransformer: {name}")
                print(cols)

                missing = set(cols) - set(df.columns)
                print("MISSING:", missing)

        print("=== END DEBUG ===\n")
        print(df.dtypes)

        # Prédiction
        score = pipe.predict_proba(df)[0][1]
        decision = "ACCORDÉ" if score < threshold else "REFUSÉ"

        return decision, float(score), float(threshold)

    except Exception as e:
        return f"ERREUR : {str(e)}", None, None


# Génération automatique des inputs Gradio AVEC VALEURS PAR DÉFAUT
inputs = []
for col in expected_cols:
    val = example[col]

    if isinstance(val, str):
        inputs.append(gr.Textbox(label=col, value=val))
    else:
        inputs.append(gr.Number(label=col, value=float(val)))

# Sorties Gradio
outputs = [
    gr.Textbox(label="Décision"),
    gr.Number(label="Score"),
    gr.Number(label="Seuil Optimal"),]

# Interface Gradio
app = gr.Interface(
    fn=predict_gradio,
    inputs=inputs,
    outputs=outputs,
    title="Scoring Crédit - Interface Gradio",
    description="Interface interactive pour tester le modèle de scoring crédit.")

app.launch()
