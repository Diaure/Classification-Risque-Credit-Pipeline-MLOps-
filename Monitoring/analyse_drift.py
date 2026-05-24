import pandas as pd
import joblib
from sklearn import datasets
from evidently.report import Report
from evidently.metrics import (DataDriftPreset, TargetDriftPreset, DataQualityPreset)

from pathlib import Path

# Charger les features via le pipeline d'entrainement
pipe = joblib.load("./BestModel/pipeline_complet.joblib")
df_example = joblib.load("./data/app_test_clean_v2.joblib")

# Récupérer les colonnes attendues par le pipeline
expected_cols = pipe.feature_names_in_
df_reference = df_example[expected_cols].copy()
print(f"Référence : {df_reference.shape[0]} lignes")


# Charger les logs opérationnels et métier
data_production = Path("logs/predictions_log.parquet")
df_production = pd.read_parquet(data_production)
print(f"Production : {df_production.shape[0]} lignes") 
df_reference["score"] = df_production["score"].copy()

# Aligner les colonnes
common_cols = list(set(df_reference.columns).intersection(df_production.columns))
df_reference = df_reference[common_cols]
df_production = df_production[common_cols]

# Chemin d'enregistrement du rapport
output_html = Path("Monitoring/drift_report.html")

# Rapport
def generer_rapport(df_reference, df_production):
    report = Report(metrics=[DataQualityPreset(), DataDriftPreset(), TargetDriftPreset()])
    report.save_html(output_html)

    print(f"Rapport généré : {output_html}")

if __name__ == "__main__":
    # df_ref, df_prod = df_reference, df_reference
    generer_rapport(df_reference = df_reference, df_production = df_production)