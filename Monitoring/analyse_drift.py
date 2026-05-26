import pandas as pd
import joblib
from sklearn import datasets
from evidently.report import Report
from evidently.metrics import (DatasetDriftMetric, DatasetMissingValuesMetric, DatasetSummaryMetric,
                                DataQualityStabilityMetric)

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
# df_reference["score"] = df_production["score"].copy()

# Aligner les colonnes
common_cols = list(set(df_reference.columns).intersection(df_production.columns))
df_reference = df_reference[common_cols]
df_production = df_production[common_cols]

# Supprimer les colonnes vides dans df_production
empty_cols = [col for col in df_production.columns if df_production[col].isna().all()]
if empty_cols:
    print("Colonnes vides supprimées :", empty_cols)
    df_production = df_production.drop(columns=empty_cols)
    df_reference = df_reference.drop(columns=empty_cols, errors="ignore")

# Supprimer les colonnes avec un seul type dans un dataset et un autre type dans l'autre
# bad_type_cols = []
# for col in df_reference.columns:
#     if col in df_production.columns:
#         if df_reference[col].dtype != df_production[col].dtype:
#             bad_type_cols.append(col)

# df_reference = df_reference.drop(columns=bad_type_cols, errors="ignore")
# df_production = df_production.drop(columns=bad_type_cols, errors="ignore")

# Supprimer les colonnes catégorielles avec catégories incompatibles
# bad_cat_cols = []
# for col in df_reference.columns:
#     if df_reference[col].dtype == "object":
#         ref_vals = set(df_reference[col].dropna().unique())
#         prod_vals = set(df_production[col].dropna().unique())
#         if len(ref_vals.intersection(prod_vals)) == 0:
#             bad_cat_cols.append(col)

# df_reference = df_reference.drop(columns=bad_cat_cols, errors="ignore")
# df_production = df_production.drop(columns=bad_cat_cols, errors="ignore")

# Supprimer les colonnes constantes (1 seule valeur)
# constant_cols = []
# for col in df_reference.columns:
#     if df_reference[col].nunique() <= 1 or df_production[col].nunique() <= 1:
#         constant_cols.append(col)

# df_reference = df_reference.drop(columns=constant_cols, errors="ignore")
# df_production = df_production.drop(columns=constant_cols, errors="ignore")

# print("Colonnes supprimées :")
# print(" - vides :", empty_cols)
# print(" - types incompatibles :", bad_type_cols)
# print(" - catégories incompatibles :", bad_cat_cols)
# print(" - constantes :", constant_cols)

# Chemin d'enregistrement du rapport
output_html = Path("Monitoring/drift_report.html")

# Garder uniquement les colonnes numériques valides
numeric_cols = [
    col for col in df_reference.columns
    if pd.api.types.is_numeric_dtype(df_reference[col]) 
    and pd.api.types.is_numeric_dtype(df_production[col])]

df_reference = df_reference[numeric_cols]
df_production = df_production[numeric_cols]

print(f"Colonnes numériques conservées ({len(numeric_cols)}) :", numeric_cols)

valid_cols = []

print("\n=== Test de stabilité colonne par colonne ===")

for col in df_reference.columns:
    try:
        test_report = Report(metrics=[DatasetDriftMetric()])
        test_report.run(
            reference_data=df_reference[[col]],
            current_data=df_production[[col]]
        )
        valid_cols.append(col)
    except Exception as e:
        print(f"Colonne exclue (instable) : {col} -> {type(e).__name__}")

df_reference = df_reference[valid_cols]
df_production = df_production[valid_cols]

print(f"\nColonnes conservées ({len(valid_cols)}) : {valid_cols}")

# Rapport
def generer_rapport(df_reference, df_production):
    report = Report(metrics=[DatasetDriftMetric(), DatasetMissingValuesMetric(), 
                             DatasetSummaryMetric(), DataQualityStabilityMetric()])
    report.run(reference_data=df_reference, current_data=df_production)
    report.save_html(output_html)

    print(f"Rapport généré : {output_html}")

if __name__ == "__main__":
    generer_rapport(df_reference = df_reference, df_production = df_production)