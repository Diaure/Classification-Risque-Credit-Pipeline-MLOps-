import pandas as pd
import joblib
from pathlib import Path

from evidently.report import Report
from evidently.metrics import (
    DatasetDriftMetric,
    DatasetMissingValuesMetric,
    DatasetSummaryMetric,)

# Charger le pipeline
pipe = joblib.load("./BestModel/pipeline_complet.joblib")
df_example = joblib.load("./data/app_test_clean_v2.joblib")

expected_cols = pipe.feature_names_in_
df_reference = df_example[expected_cols].copy()

# Charger production
df_production = pd.read_parquet("logs/predictions_log.parquet")

# Colonnes communes
common_cols = list(set(df_reference.columns).intersection(df_production.columns))
df_reference = df_reference[common_cols]
df_production = df_production[common_cols]

# Garder uniquement les colonnes numériques
numeric_cols = [
    col for col in df_reference.columns
    if pd.api.types.is_numeric_dtype(df_reference[col])
    and pd.api.types.is_numeric_dtype(df_production[col])]

df_reference = df_reference[numeric_cols]
df_production = df_production[numeric_cols]

print(f"Colonnes numériques conservées ({len(numeric_cols)}) :", numeric_cols)

# Rapport Evidently
report = Report(metrics=[
    DatasetSummaryMetric(),
    DatasetMissingValuesMetric(),
    DatasetDriftMetric(),])

report.run(reference_data=df_reference, current_data=df_production)
report.save_html("Monitoring/drift_report.html")

print("Rapport généré.")
