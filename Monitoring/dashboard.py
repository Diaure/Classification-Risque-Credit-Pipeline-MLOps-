import streamlit as st
import pandas as pd
import json
import plotly.express as px
from pathlib import Path
import plotly.graph_objects as go


st.set_page_config(page_title="Monitoring Drift", layout="wide")

# Charger le rapport Evidently
with open("Monitoring/drift_report.json", "r", encoding="utf-8") as f:
    drift_data = json.load(f)

# Tests pour vérifier la structure du json drift
# for m in drift_data["metrics"]:
#     if m["metric"] == "ColumnSummaryMetric":
#         st.json(m)
#         break

# for m in drift_data["metrics"]:
#     if m["metric"] == "ColumnSummaryMetric":
#         print("======")
#         print(m.keys())
#         print(m["result"].keys())
#         break

# for m in drift_data["metrics"]:
#     if m["metric"] == "ColumnDriftMetric":
#         st.json(m)
#         break

# metrics_names = set(
#     m["metric"]
#     for m in drift_data["metrics"])
# st.write(metrics_names)
# st.json(drift_data["metrics"][0])

# Charger les logs bruts
df_logs = pd.read_parquet("logs/predictions_log.parquet")

st.title("📊 Monitoring du Drift — Dashboard MLOps")

# ONGLET 1 — Vue d’ensemble
tab1, tab2, tab3, tab4 = st.tabs(["VUE D'ENSEMBLE", "DERIVE PAR COLONNE", "RESUME PAR COLONNE", "LOGS BRUTS"])

with tab1:
    # Colonnes en dérive - Résultat global
    dataset_drift = next(
    m for m in drift_data["metrics"]
    if m["metric"] == "DatasetDriftMetric")

    drift_res = dataset_drift["result"]

    with st.container():
        st.markdown("""<p style='font-size: 22px; font-style: italic;'>Performance Globale Colonnes</p>""", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns([1,1,1,1])

        st.markdown("<br>", unsafe_allow_html=True)
        col1.metric("Prédictions", len(df_logs))
        col2.metric("Colonnes analysées", drift_res["number_of_columns"])
        col3.metric("Colonnes en dérive",  drift_res["number_of_drifted_columns"])
        col4.metric( "Taux de dérive", f"{100*drift_res['share_of_drifted_columns']:.1f}%")

    # KPI API
    with st.container():
        st.markdown("""<p style='font-size: 22px; font-style: italic;'>Performance API</p>""", unsafe_allow_html=True)
        c1, c2, c3, c4, c5 = st.columns([1,1,1,1,1])

        st.markdown("<br>", unsafe_allow_html=True)
        c1.metric("Latence moyenne", f"{df_logs['latency_ms'].mean():.1f}%")
        c2.metric("CPU moyen", f"{df_logs['cpu_percent'].mean():.1f}%")
        c3.metric("RAM moyenne", f"{df_logs['ram_percent'].mean():.1f}%")
        c4.metric("Charge système", f"{df_logs['system_load'].mean():.2f}")
        c5.metric("Threads moyens", f"{df_logs['num_threads'].mean():.0f}")

    # KPI Métier
    with st.container():
        st.markdown("""<p style='font-size: 22px; font-style: italic;'>Performance Métier</p>""", unsafe_allow_html=True)
        m1, m2, m3 = st.columns([1,1,1])
        
        st.markdown("<br>", unsafe_allow_html=True)
        m1.metric("Score moyen", f"{df_logs['score_x'].mean():.3f}")
        m2.metric("Seuil optimal moyen", f"{df_logs['threshold_x'].mean():.3f}")
        m3.metric("Décision majoritaire", df_logs["decision_x"].mode()[0])

    # Graphique distribution décisions
    decision_df = (df_logs["decision_x"].value_counts().reset_index())
    fig = px.bar(decision_df, x = "decision_x", y = "count", title = "Répartition des décisions")
    st.plotly_chart(fig, use_container_width = True)

    # Graphique distribution colonnes en dérive
    drift_graph = pd.DataFrame({
        "Etat": [
            "En dérive",
            "Sans dérive"],
        "Nombre": [
            drift_res["number_of_drifted_columns"],
            drift_res["number_of_columns"]
            - drift_res["number_of_drifted_columns"]]})

    fig = px.bar(drift_graph, x = "Etat", y = "Nombre", title = "Répartition des colonnes en dérive")
    st.plotly_chart(fig, use_container_width = True)


    # Liste des colonnes en drift
    drifted_cols = []
    for m in drift_data["metrics"]:
        if m["metric"] != "ColumnDriftMetric":
            continue
        if m['result']['drift_detected']:
            drifted_cols.append(m["result"]["column_name"])
    
    st.subheader("Colonnes en dérive")
    st.write(drifted_cols)

# ONGLET 2 — Dérive par colonne
with tab2:
    st.header("📈 Dérive par colonne")

    summary_dict = {}

    for m in drift_data["metrics"]:
        if m["metric"] != "ColumnSummaryMetric":
            continue
        
        result = m['result']

        # summary_dict[m[result]["column_name"]] = m[result]
        # summary_dict[result["column_name"]] = {
        #     "missing": result["current_characteristics"]["missing"],
        #     "missing_pct": result["current_characteristics"]["missing_percentage"]}
        
        summary_dict[result["column_name"]] = {
        "missing": result["current_characteristics"]["missing"],
        "missing_pct": result["current_characteristics"]["missing_percentage"],
        "unique": result["current_characteristics"]["unique"]}

    # print(list(summary_dict.keys())[:5])

    drift_rows = []
    for m in drift_data["metrics"]:
        if m["metric"] != "ColumnDriftMetric":
            continue
        
        result = m['result']
        col = result["column_name"]
        # missing_data = (summary_dict[col]["current_characteristics"]["missing"])

        drift_rows.append({
            "Colonne": col,
            "Type": result["column_type"],
            "Distance drift": result["drift_score"],
            "Dérive(%)": round(result["drift_score"] * 100, 2),
            "Seuil(%)": round(result["stattest_threshold"] * 100, 2),
            "Drift détecté": result["drift_detected"],
            "Test": result["stattest_name"],
            "Nombre valeurs manquantes": summary_dict[col]["missing"],
            "Taux valeurs manquantes": summary_dict[col]["missing_pct"],
            "Nombre de valeurs uniques": summary_dict[col]["unique"]})
        
    df_drift = pd.DataFrame(drift_rows)
    st.dataframe(df_drift.sort_values("Distance drift", ascending = False),  use_container_width = True)
    
    selected_col = st.selectbox("Choisir une colonne", df_drift["Colonne"], key = "drift_column")

    metric = next(m for m in drift_data["metrics"]if (m["metric"] == "ColumnDriftMetric" and m["result"]["column_name"] == selected_col))
    x_ref = metric["result"]["reference"]["small_distribution"]["x"]
    y_ref = metric["result"]["reference"]["small_distribution"]["y"]

    x_cur = metric["result"]["current"]["small_distribution"]["x"]
    y_cur = metric["result"]["current"]["small_distribution"]["y"]

    st.write(f"Distribution de {selected_col}")  
    fig = go.Figure()
    fig.add_bar(x = x_ref, y = y_ref, name = "Référence")
    fig.add_bar(x = x_cur, y = y_cur, name = "Production")
    fig.update_layout(barmode="group", title = f"Distribution - {selected_col}", xaxis_title = "Valeurs", yaxis_title = "Densité", legend_title = "")

    st.plotly_chart(fig, use_container_width = True)


# ONGLET 3 — Résumé par colonne (finalement faire plutôt un tableau?)
with tab3:
    st.header("📘 Résumé statistique par colonne")

    summaries = {}
    for m in drift_data["metrics"]:
        if m["metric"] != "ColumnSummaryMetric":
            continue

        result2 = m['result']
        summaries[result2["column_name"]] = result2

        col_selectione = st.selectbox("Choisir une colonne", sorted(summaries.keys()))
        summary = summaries[col_selectione]

        ref = summary["reference_characteristics"]
        cur = summary["current_characteristics"]

        # col = result2["column_name"]
        st.subheader(f"🔹 {col_selectione}")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Référence")
            st.dataframe(
                pd.DataFrame(
                    ref.items(),
                    columns=["Métrique", "Valeur"]
                ),
                use_container_width = True)

        with col2:
            st.markdown("### Production")
            st.dataframe(pd.DataFrame(cur.items(), columns=["Métrique", "Valeur"]), use_container_width = True)

        # comparaison synthétique
        compare_df = pd.DataFrame({
            "Métrique": [
                "count",
                "missing",
                "mean",
                "std",
                "min",
                "p25",
                "p50",
                "p75",
                "max",
                "unique"
            ],
            "Référence": [
                ref.get("count"),
                ref.get("missing"),
                ref.get("mean"),
                ref.get("std"),
                ref.get("min"),
                ref.get("p25"),
                ref.get("p50"),
                ref.get("p75"),
                ref.get("max"),
                ref.get("unique")
            ],
            "Production": [
                cur.get("count"),
                cur.get("missing"),
                cur.get("mean"),
                cur.get("std"),
                cur.get("min"),
                cur.get("p25"),
                cur.get("p50"),
                cur.get("p75"),
                cur.get("max"),
                cur.get("unique")
            ]})

        st.markdown("### Comparaison directe")
        st.dataframe(compare_df, use_container_width = True)

# ONGLET 4 — Logs bruts
with tab4:
    st.header("📄 Logs bruts (production)")

    st.dataframe(df_logs.head(200))

    col = st.selectbox("Visualiser une colonne :", df_logs.columns)

    fig = px.histogram(df_logs, x=col, nbins=30, title=f"Distribution de {col}")
    st.plotly_chart(fig, use_container_width=True)
