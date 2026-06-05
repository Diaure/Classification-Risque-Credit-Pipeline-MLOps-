import streamlit as st
import pandas as pd
import json
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Monitoring Drift", layout="wide")

# Charger le rapport Evidently
with open("Monitoring/drift_report.json", "r", encoding="utf-8") as f:
    drift_data = json.load(f)

# Tests pour vérifier la structure du json drift
for m in drift_data["metrics"]:
    if m["metric"] == "ColumnSummaryMetric":
        st.json(m)
        break

for m in drift_data["metrics"]:
    if m["metric"] == "ColumnDriftMetric":
        st.json(m)
        break

metrics_names = set(
    m["metric"]
    for m in drift_data["metrics"])
st.write(metrics_names)

st.json(drift_data["metrics"][0])

# Charger les logs bruts
df_logs = pd.read_parquet("logs/predictions_log.parquet")

st.title("📊 Monitoring du Drift — Dashboard MLOps")


# ONGLET 1 — Vue d’ensemble
tab1, tab2, tab3, tab4 = st.tabs(["Vue d’ensemble", "Dérive par colonne", "Résumé par colonne", "Logs bruts"])

with tab1:
    st.header("📌 Vue d’ensemble")

    # Nombre de colonnes analysées
    # nb_cols = len(drift_data["metrics"])
    nb_cols = sum(1
    for m in drift_data["metrics"]
    if m["metric"] == "ColumnDriftMetric")
    st.metric("Nombre de colonnes analysées", nb_cols)

    # Colonnes en dérive - Résultat global
    dataset_drift = next(
    m for m in drift_data["metrics"]
    if m["metric"] == "DatasetDriftMetric")

    st.metric("Colonnes en dérive", dataset_drift["result"]["number_of_drifted_columns"])
    st.metric("Taux dérive", round(dataset_drift["result"]["share_of_drifted_columns"] * 100, 1))

    # Affichage des colonnes en drift
    drifted_cols = []
    for m in drift_data["metrics"]:
        if m["metric"] != "ColumnDriftMetric":
            continue
        if m['result']['drift_detected']:
            drifted_cols.append(m["result"]["column_name"])
    
    st.subheader("Colonnes en dérive")
    if drifted_cols:
        st.error(drifted_cols)
    else:
        st.success("Aucune dérive détectée")

# ONGLET 2 — Dérive par colonne
with tab2:
    st.header("📈 Dérive par colonne")

    for m in drift_data["metrics"]:
        if m["metric"] != "ColumnDriftMetric":
            continue

        result = m['result']
        col = result["column_name"]
        drift = result["drift_detected"]
        score = result["drift_score"]
        stat = result["stattest_name"]
        # p_value = result["p_value"]

        st.subheader(f"🔹 {col}")
        st.write(f"Score : **{score}: {score:.4f} **")
        # st.write(f"Test : **{stat}** — p-value = **{p_value:.4f}**")

        if drift:
            st.error("Dérive détectée")
        else:
            st.success("Pas de dérive")

# ONGLET 3 — Résumé par colonne (finalement faire plutôt un tableau?)
with tab3:
    st.header("📘 Résumé statistique par colonne")

    for m in drift_data["metrics"]:
        if m["metric"] != "ColumnDriftMetric":
            continue

        result2 = m['result']
        col = result2["column_name"]
        st.subheader(f"🔹 {col}")

        summary = m["result"]
        st.json(summary)

# ONGLET 4 — Logs bruts
with tab4:
    st.header("📄 Logs bruts (production)")

    st.dataframe(df_logs.head(200))

    col = st.selectbox("Visualiser une colonne :", df_logs.columns)

    fig = px.histogram(df_logs, x=col, nbins=30, title=f"Distribution de {col}")
    st.plotly_chart(fig, use_container_width=True)
