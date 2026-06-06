import pandas as pd
import joblib

from evidently.report import Report
from evidently.metrics import (
    DatasetSummaryMetric,
    DatasetMissingValuesMetric,
    ColumnSummaryMetric,
    DatasetDriftMetric,
    ColumnDriftMetric,
)
from evidently.metrics import ColumnDriftMetric

# =========================
# Chargement des données
# =========================

pipe = joblib.load("./BestModel/pipeline_complet.joblib")
df_example = joblib.load("./data/app_test_clean_v2.joblib")

expected_cols = pipe.feature_names_in_

# df_reference = df_example[expected_cols].copy()
X_ref = pipe[:-1].transform(df_example)
df_reference = pd.DataFrame(X_ref, columns=pipe[:-1].get_feature_names_out())
print(df_reference.shape)
print(df_reference.columns[:20])

df_production = pd.read_parquet("logs/predictions_log.parquet")
print(df_production.shape)
print(df_production.columns[:20])

print(len(set(df_reference.columns).intersection(df_production.columns)))

# =========================
# Colonnes communes
# =========================

df_reference.columns = df_reference.columns.astype(str)
df_production.columns = df_production.columns.astype(str)

common_cols = sorted(
    set(df_reference.columns)
    .intersection(df_production.columns))

for col in common_cols:

    ref_num = pd.api.types.is_numeric_dtype(df_reference[col])
    prod_num = pd.api.types.is_numeric_dtype(df_production[col])

    if ref_num and prod_num:

        df_reference[col] = pd.to_numeric(
            df_reference[col],
            errors="coerce"
        )

        df_production[col] = pd.to_numeric(
            df_production[col],
            errors="coerce"
        )

    else:

        df_reference[col] = (
            df_reference[col]
            .fillna("MISSING")
            .astype(str))

        df_production[col] = (
            df_production[col]
            .fillna("MISSING")
            .astype(str))
        
for col in common_cols:

    if not pd.api.types.is_numeric_dtype(df_reference[col]):

        assert (
            df_reference[col]
            .dropna()
            .map(type)
            .eq(str)
            .all()
        )

        assert (
            df_production[col]
            .dropna()
            .map(type)
            .eq(str)
            .all()
        )

df_reference = df_reference[common_cols].copy()
df_production = df_production[common_cols].copy()

# Conversion bool en int
for col in common_cols:
    if df_reference[col].dtype == bool:
        df_reference[col] = df_reference[col].astype(int)
    if df_production[col].dtype == bool:
        df_production[col] = df_production[col].astype(int)

# Harmonisation robuste
for col in common_cols:
    ref_types = set(df_reference[col].dropna().map(type))
    prod_types = set(df_production[col].dropna().map(type))
    all_types = ref_types.union(prod_types)
    ref_num = pd.api.types.is_numeric_dtype(df_reference[col])

    prod_num = pd.api.types.is_numeric_dtype(df_production[col])
    # Mélange de types Python
    if len(all_types) > 1:
        print(f"Conversion forcée en str : {col}")
        df_reference[col] = (df_reference[col].fillna("MISSING").astype(str))
        df_production[col] = (df_production[col].fillna("MISSING").astype(str))
    # Numérique des deux côtés
    elif ref_num and prod_num:
        df_reference[col] = pd.to_numeric(df_reference[col], errors="coerce")
        df_production[col] = pd.to_numeric(df_production[col], errors="coerce")
    # Catégoriel
    else:
        df_reference[col] = (df_reference[col].fillna("MISSING").astype(str))
        df_production[col] = (df_production[col].fillna("MISSING").astype(str))

# Colonnes vides
valid_cols = []
for col in common_cols:
    if(df_reference[col].notna().sum() > 0 and df_production[col].notna().sum() > 0):
        valid_cols.append(col)

df_reference = df_reference[valid_cols]
df_production = df_production[valid_cols]

# Colonnes constantes
non_constant_cols = []
for col in valid_cols:
    if (df_reference[col].nunique(dropna=True) > 1 and df_production[col].nunique(dropna=True) > 1):
        non_constant_cols.append(col)

df_reference = df_reference[non_constant_cols]
df_production = df_production[non_constant_cols]

# Vérification finale
print("\n=== TYPES FINAUX ===")
for col in df_reference.columns:
    if df_reference[col].dtype != df_production[col].dtype:
        print(
            f"Mismatch : {col} -> "
            f"{df_reference[col].dtype} / "
            f"{df_production[col].dtype}")

print("\nNb colonnes finales :", len(df_reference.columns))

print(df_reference.shape)
print(df_production.shape)

print(len(set(df_reference.columns).intersection(df_production.columns)))

print(df_reference.columns[:20].tolist())
print(df_production.columns[:20].tolist())

print(set(df_reference.columns) - set(df_production.columns))


print(df_production.describe().T)
df_production.nunique().sort_values()

print(df_reference.columns.tolist()[:50])

# Rapport Evidently
metrics = [
    DatasetSummaryMetric(),
    DatasetMissingValuesMetric(),
    DatasetDriftMetric(),]

for col in df_reference.columns:
    metrics.append(ColumnSummaryMetric(column_name=col))
    metrics.append(ColumnDriftMetric(column_name=col))

print("\n=== RECHERCHE COLONNE PROBLEMATIQUE ===")
for col in df_reference.columns:

    ref_types = set(type(x) for x in df_reference[col].dropna().unique())
    prod_types = set(type(x) for x in df_production[col].dropna().unique())

    if len(ref_types.union(prod_types)) > 1:
        print(
            f"{col}\n"
            f" REF={ref_types}\n"
            f" PROD={prod_types}\n")

report = Report(metrics=metrics)
report.run(reference_data=df_reference, current_data=df_production,)

report.save_html("Monitoring/drift_report.html")
report.save_json("Monitoring/drift_report.json")

print("\nRapport généré : "
      "Monitoring/drift_report.json")