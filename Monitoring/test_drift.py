import pandas as pd
import joblib

from evidently.report import Report
from evidently.metrics import ColumnDriftMetric

# =========================
# Chargement des données
# =========================

pipe = joblib.load("./BestModel/pipeline_complet.joblib")
df_example = joblib.load("./data/app_test_clean_v2.joblib")

expected_cols = pipe.feature_names_in_

df_reference = df_example[expected_cols].copy()

df_production = pd.read_parquet(
    "logs/predictions_log.parquet"
)

# =========================
# Colonnes communes
# =========================

df_reference.columns = df_reference.columns.astype(str)
df_production.columns = df_production.columns.astype(str)

common_cols = sorted(
    set(df_reference.columns)
    .intersection(df_production.columns)
)

df_reference = df_reference[common_cols].copy()
df_production = df_production[common_cols].copy()

# =========================
# Harmonisation des types
# =========================

for col in common_cols:

    # bool -> int
    if df_reference[col].dtype == bool:
        df_reference[col] = df_reference[col].astype(int)

    if df_production[col].dtype == bool:
        df_production[col] = df_production[col].astype(int)

    ref_num = pd.api.types.is_numeric_dtype(df_reference[col])
    prod_num = pd.api.types.is_numeric_dtype(df_production[col])

    # Les deux numériques
    if ref_num and prod_num:

        df_reference[col] = (
            pd.to_numeric(
                df_reference[col],
                errors="coerce"
            )
            .astype("float64")
        )

        df_production[col] = (
            pd.to_numeric(
                df_production[col],
                errors="coerce"
            )
            .astype("float64")
        )

    # Sinon tout en string
    else:

        df_reference[col] = (
            df_reference[col]
            .fillna("MISSING")
            .astype(str)
        )

        df_production[col] = (
            df_production[col]
            .fillna("MISSING")
            .astype(str)
        )

# =========================
# Suppression colonnes vides
# =========================

valid_cols = []

for col in common_cols:

    if (
        df_reference[col].notna().sum() > 0
        and
        df_production[col].notna().sum() > 0
    ):
        valid_cols.append(col)

df_reference = df_reference[valid_cols]
df_production = df_production[valid_cols]

# =========================
# Suppression colonnes constantes
# =========================

non_constant_cols = []

for col in valid_cols:

    if (
        df_reference[col].nunique(dropna=True) > 1
        and
        df_production[col].nunique(dropna=True) > 1
    ):
        non_constant_cols.append(col)

df_reference = df_reference[non_constant_cols]
df_production = df_production[non_constant_cols]

print(f"\nNombre de colonnes testées : {len(non_constant_cols)}")

# =========================
# Test colonne par colonne
# =========================

for col in non_constant_cols:

    print(f"\nTest : {col}")

    try:

        report = Report(
            metrics=[
                ColumnDriftMetric(column_name=col)
            ]
        )

        report.run(
            reference_data=df_reference[[col]],
            current_data=df_production[[col]]
        )

        print("OK")

    except Exception as e:

        print("\n===================================")
        print(f"COLONNE EN ERREUR : {col}")
        print("===================================")

        print("\nType référence :")
        print(df_reference[col].dtype)

        print("\nType production :")
        print(df_production[col].dtype)

        print("\nTypes Python REF :")
        print(
            set(
                df_reference[col]
                .dropna()
                .map(type)
            )
        )

        print("\nTypes Python PROD :")
        print(
            set(
                df_production[col]
                .dropna()
                .map(type)
            )
        )

        print("\nException :")
        print(e)

        break

print(df_reference.shape)
print(df_production.shape)

print(set(df_production.columns) - set(df_reference.columns))
print(set(df_reference.columns) - set(df_production.columns))

print("\nFin du diagnostic.")