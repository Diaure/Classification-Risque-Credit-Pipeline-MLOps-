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

# # Tests pour vérifier la structure du json drift
# for m in drift_data["metrics"]:
#     if m["metric"] == "ColumnSummaryMetric":
#         st.json(m)
#         break

# for m in drift_data["metrics"]:
#     if m["metric"] == "ColumnSummaryMetric":
#         st.write(m)
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
df_logs["timestamp"] = pd.to_datetime(df_logs["timestamp_x"], unit="s")

# Charger les logs après optimisation
df_logs_opti = pd.read_parquet("logs/predictions_log_batch.parquet")
df_logs_opti["timestamp_model"] = pd.to_datetime(df_logs_opti["timestamp_model"], unit="s")

# st.write(df_logs.head())
# st.write(df_logs_opti.head())

st.title("📊 Monitoring du Drift — Dashboard MLOps")

# ONGLET 1 — Vue d’ensemble
tab1, tab2, tab3, tab4, tab5 = st.tabs(["VUE D'ENSEMBLE", "DERIVE PAR COLONNE", "LOGS BRUTS", "IMPACT OPTIMISATION", "COMPARAISON UNITAIRE vs BATCH"])

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
        c1, c2, c3, c4, c5, c6 = st.columns([1,1,1,1,1,1])

        st.markdown("<br>", unsafe_allow_html=True)
        c1.metric("Latence moyenne", f"{df_logs['latency_ms'].mean():.2f}")
        c2.metric("Temps d'inférence moyen", f"{df_logs['inference_ms_x'].mean():.2f}")
        c3.metric("CPU moyen", f"{df_logs['cpu_percent'].mean():.1f}%")
        c4.metric("RAM moyenne", f"{df_logs['ram_percent'].mean():.1f}%")
        c5.metric("Charge système", f"{df_logs['system_load'].mean():.2f}")
        c6.metric("Threads moyens", f"{df_logs['num_threads'].mean():.0f}")

    # KPI Métier
    with st.container():
        st.markdown("""<p style='font-size: 22px; font-style: italic;'>Performance Métier</p>""", unsafe_allow_html=True)
        m1, m2, m3 = st.columns([1,1,1])
        
        st.markdown("<br>", unsafe_allow_html=True)
        m1.metric("Probalité moyenne", f"{df_logs['score_x'].mean():.2f}")
        m2.metric("Seuil optimal moyen", f"{df_logs['threshold_x'].mean():.3f}")
        m3.metric("Décision majoritaire", df_logs["decision_x"].mode()[0])

    with st.container():
        g1, g2 = st.columns([1,1])
        
        # Graphique distribution des scores
        score_df = (df_logs["score_x"].value_counts().reset_index())
        fig = px.bar(score_df, x = "score_x", y = "count", title = "Répartition des scores")
        g1.plotly_chart(fig, width = "stretch")

        # Graphique distribution décisions
        decision_df = (df_logs["decision_x"].value_counts().reset_index())
        fig = px.bar(decision_df, x = "decision_x", y = "count", title = "Répartition des décisions")
        g2.plotly_chart(fig, width = "stretch")

    with st.container():
        h1, h2, h3 = st.columns([1,1,1])

        # Latence dans le temps
        fig = px.line(df_logs, x="timestamp", y="latency_ms", title = "Distribution de la latence dans le temps")
        h1.plotly_chart(fig, width = "stretch")

        # CPU dans le temps
        fig = px.line(df_logs, x="timestamp", y="cpu_percent", title = "Distribution du CPU dans le temps")
        h2.plotly_chart(fig, width = "stretch")

        # RAM dans le temps
        fig = px.line(df_logs, x="timestamp", y="ram_percent", title = "Distribution de la RAM dans le temps")
        h3.plotly_chart(fig, width = "stretch")

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
    st.plotly_chart(fig, width = "stretch")


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
        summary_dict[result["column_name"]] = {
        "missing": result["current_characteristics"]["missing"],
        "missing_pct": result["current_characteristics"]["missing_percentage"],
        "unique": result["current_characteristics"]["unique"]}

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
    df_drift_filtered = (df_drift[df_drift["Drift détecté"] == True].drop_duplicates(subset=["Colonne"])) # uniquement les colonnes en dérive pour voir le taux de dérive par colonne
    # st.dataframe(df_drift_filtered.sort_values("Distance drift", ascending = False),  width = "stretch")
    
    selected_col = st.selectbox("Choisir une colonne", df_drift_filtered["Colonne"], key = "drift_column")

    col_stats = df_drift_filtered[df_drift_filtered["Colonne"] == selected_col].iloc[0]
    
    metric = next(m for m in drift_data["metrics"]if (m["metric"] == "ColumnDriftMetric" and m["result"]["column_name"] == selected_col))
    x_ref = metric["result"]["reference"]["small_distribution"]["x"]
    y_ref = metric["result"]["reference"]["small_distribution"]["y"]

    x_cur = metric["result"]["current"]["small_distribution"]["x"]
    y_cur = metric["result"]["current"]["small_distribution"]["y"]

    summary_metric = next(m for m in drift_data["metrics"] if (m["metric"] == "ColumnSummaryMetric" and m["result"]["column_name"] == selected_col))
    missing_ref = summary_metric["result"]["reference_characteristics"]["missing"]
    missing_cur = summary_metric["result"]["current_characteristics"]["missing"]

    with st.container():
        st.write(f"Analyse détaillée: {selected_col}")  

        st.markdown(f"""
    - **Distance drift** : `{col_stats['Distance drift']:.4f}`
    - **Dérive (%)** : `{col_stats['Dérive(%)']} %`
    - **Seuil (%)** : `{col_stats['Seuil(%)']} %`
    - **Drift détecté** : `{"Oui" if col_stats['Drift détecté'] else "Non"}`
    """)
        
        d1, d2 = st.columns([1,1])    

        # Distribution des données
        fig = go.Figure()
        fig.add_bar(x = x_ref, y = y_ref, name = "Référence")
        fig.add_bar(x = x_cur, y = y_cur, name = "Production")
        fig.update_layout(barmode = "group", title = f"Distribution - {selected_col}", xaxis_title = "Valeurs", yaxis_title = "Densité", legend_title = "")
        d1.plotly_chart(fig, width = "stretch")

        # Distribution valeurs manquantes
        fig_missing = go.Figure()
        fig_missing.add_bar(x = ["Référence"], y = [missing_ref], name = "Référence")
        fig_missing.add_bar(x = ["Production"], y = [missing_cur], name = "Production")
        fig_missing.update_layout(barmode="group", title=f"Valeurs manquantes - {selected_col}", yaxis_title = "Nombre de valeurs manquantes")

        d2.plotly_chart(fig_missing, width = "stretch")

# ONGLET 3 — Résumé par colonne (finalement faire plutôt un tableau?)
# with tab3:
#     st.header("📘 Résumé statistique par colonne")

#     summaries = {}
#     for m in drift_data["metrics"]:
#         if m["metric"] != "ColumnSummaryMetric": 
#             continue
#         result2 = m['result']

#         if ("column_name" not in result2 or result2["column_name"] is None or "reference_characteristics" not in result2 or "current_characteristics" not in result2):
#                 continue
#         summaries[result2["column_name"]] = result2

#     options = sorted(summaries.keys())

#     col_selectione = st.selectbox("Choisir une colonne", options, index=0)
#     # col_selectione = st.selectbox("Choisir une colonne", sorted(summaries.keys()), key="summary_column")

#     summary = summaries[col_selectione]
#     ref = summary["reference_characteristics"]
#     cur = summary["current_characteristics"]

#     st.subheader(f"🔹 {col_selectione}")
#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("### Référence")
#         st.dataframe(pd.DataFrame(ref.items(), columns=["Métrique", "Valeur"]), width = True)

#     with col2:
#         st.markdown("### Production")
#         st.dataframe(pd.DataFrame(cur.items(), columns=["Métrique", "Valeur"]), width = True)

#     # comparaison synthétique
#     compare_df = pd.DataFrame({
#             "Métrique": ["count", "missing", "mean", "std", "min", "p25", "p50", "p75", "max", "unique"],
#             "Référence": [ref.get("count"), ref.get("missing"), ref.get("mean"), ref.get("std"), ref.get("min"), ref.get("p25"), 
#                           ref.get("p50"), ref.get("p75"), ref.get("max"), ref.get("unique")],
#             "Production": [cur.get("count"), cur.get("missing"), cur.get("mean"), cur.get("std"), cur.get("min"), cur.get("p25"), 
#                            cur.get("p50"), cur.get("p75"), cur.get("max"), cur.get("unique")]})

#     st.markdown("### Comparaison directe")
#     st.dataframe(compare_df, width = True)

# ONGLET 4 — Logs bruts
with tab3:
    st.header("📄 Logs bruts (production)")

    st.dataframe(df_logs.head(200))

    col = st.selectbox("Visualiser une colonne :", df_logs.columns)

    fig = px.histogram(df_logs, x=col, nbins=30, title=f"Distribution de {col}")
    st.plotly_chart(fig, width="stretch")

# ONGLET 5 - KPI API après optimisation du processing
with tab4:
    # KPI API
    with st.container():
        st.markdown("""<p style='font-size: 22px; font-style: italic;'>Performance API (Batch)</p>""", unsafe_allow_html=True)

        if df_logs_opti.empty:
            st.warning("Aucun batch n'a encore été exécuté. Lance un batch pour voir les KPI.")
        else:
            k1, k2, k3, k4, k5, k6 = st.columns([1,1,1,1,1,1])

            k1.metric("Latence moyenne", f"{df_logs_opti['latency_ms_ops'].mean():.2f}")
            k2.metric("Temps d'inférence moyen", f"{df_logs_opti['inference_ms_model'].mean():.2f}")
            k3.metric("CPU moyen", f"{df_logs_opti['cpu_percent_ops'].mean():.1f}%")
            k4.metric("RAM moyenne", f"{df_logs_opti['ram_percent_ops'].mean():.1f}%")
            k5.metric("Charge système", f"{df_logs_opti['system_load_ops'].mean():.2f}")
            k6.metric("Threads moyens", f"{df_logs_opti['num_threads_ops'].mean():.0f}")
            st.markdown("<br>", unsafe_allow_html=True)

            with st.container():
                o1, o2, o3 = st.columns([1,1,1])

                # Latence dans le temps
                fig = px.line(df_logs_opti, x="timestamp_model", y="latency_ms_ops", title = "Latence du batch dans le temps")
                o1.plotly_chart(fig, width = "stretch")

                # CPU dans le temps
                fig = px.line(df_logs_opti, x="timestamp_model", y="cpu_percent_ops", title = "CPU utilisé par le batch")
                o2.plotly_chart(fig, width = "stretch")

                # RAM dans le temps
                fig = px.line(df_logs_opti, x="timestamp_model", y="ram_percent_ops", title = "RAM dutilisé par le batch")
                o3.plotly_chart(fig, width = "stretch")

    fig = px.scatter(df_logs_opti, x = "batch_size_model", y = "latency_ms_ops", trendline = "ols", title = "Relation entre batch_size et latence")
    st.plotly_chart(fig, use_container_width=True)

# ONGLET 6 - Compaaison des kpis avant et après optimisation
with tab5:
    if df_logs.empty or df_logs_opti.empty:
        st.warning("Exécute au moins une requête unitaire et un batch pour afficher la comparaison.")
    else:
        # Calculs
        df_unit = df_logs.copy()
        df_batch = df_logs_opti.copy()

        # Latence par client
        df_unit["latence_par_client"] = df_unit["latency_ms"]
        df_batch["latence_par_client"] = df_batch["latency_ms_ops"] / df_batch["batch_size_model"]

        # Inférence par client
        df_unit["inference_par_client"] = df_unit["inference_ms_x"]
        df_batch["inference_par_client"] = df_batch["inference_ms_model"] / df_batch["batch_size_model"]

        # CPU / RAM / Load / Threads
        df_unit["cpu"] = df_unit["cpu_percent"]
        df_batch["cpu"] = df_batch["cpu_percent_ops"]

        df_unit["ram"] = df_unit["ram_percent"]
        df_batch["ram"] = df_batch["ram_percent_ops"]

        df_unit["load"] = df_unit["system_load"]
        df_batch["load"] = df_batch["system_load_ops"]

        df_unit["threads"] = df_unit["num_threads"]
        df_batch["threads"] = df_batch["num_threads_ops"]

        # KPI
        st.subheader("Performances par client")
        p1, p2, p3 = st.columns([1,1,1])

        # st.markdown("""<p style='font-size: 22px; font-style: italic;'>Latence par client</p>""", unsafe_allow_html=True)
        p1.metric("Latence par client (unitaire)", f"{df_unit['latence_par_client'].mean():.2f} ms")
        p2.metric("Latence par client (batch)", f"{df_batch['latence_par_client'].mean():.2f} ms")
        p3.metric("Gain", f"{df_unit['latence_par_client'].mean() / df_batch['latence_par_client'].mean():.1f}")
        # st.markdown("<br>", unsafe_allow_html=True)

        i1, i2, i3 = st.columns([1,1,1])

        # st.markdown("""<p style='font-size: 22px; font-style: italic;'>Inférence par client</p>""", unsafe_allow_html=True)   
        i1.metric("Inférence par client (unitaire)", f"{df_unit['inference_par_client'].mean():.2f} ms")
        i2.metric("Inférence par client (batch)", f"{df_batch['inference_par_client'].mean():.2f} ms")
        i3.metric("Gain", f"{df_unit['inference_par_client'].mean() / df_batch['inference_par_client'].mean():.1f}")
        st.markdown("<br>", unsafe_allow_html=True)

        # kpi CPU/RAM/LOAD/THREADS
        st.subheader("Charge système")

        s1, s2, s3, s4 = st.columns([1,1,1,1])
        s1.metric("CPU (%) unitaire", f"{df_unit['cpu'].mean():.1f}%")
        s2.metric("CPU (%) batch", f"{df_batch['cpu'].mean():.1f}%")
        s3.metric("RAM (%) unitaire", f"{df_unit['ram'].mean():.1f}%")
        s4.metric("RAM (%) batch", f"{df_batch['ram'].mean():.1f}%")

        s5, s6, s7, s8 = st.columns(4)
        s5.metric("Load unitaire", f"{df_unit['load'].mean():.2f}")
        s6.metric("Load batch", f"{df_batch['load'].mean():.2f}")
        s7.metric("Threads unitaire", f"{df_unit['threads'].mean():.0f}")
        s8.metric("Threads batch", f"{df_batch['threads'].mean():.0f}")
        st.markdown("<hr>", unsafe_allow_html=True)

        # Graphiques comparatifs
        st.subheader("Visualisations comparatives")
        
        c1, c2 = st.columns(2)

        fig = px.box(pd.concat([df_unit.assign(mode = "Unitaire"), df_batch.assign(mode = "Batch")]), x = "mode", y = "latence_par_client", title = "Latence par client : Unitaire vs Batch")
        c1.plotly_chart(fig, use_container_width=True)

        fig = px.box(pd.concat([df_unit.assign(mode = "Unitaire"), df_batch.assign(mode = "Batch")]), x = "mode", y = "inference_par_client", title = "Inférence par client : Unitaire vs Batch")
        c2.plotly_chart(fig, use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

        # CPU
        fig = px.box(pd.concat([df_unit.assign(mode = "Unitaire"), df_batch.assign(mode = "Batch")]), x = "mode", y = "cpu", title = "CPU (%) : Unitaire vs Batch")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

        # RAM
        fig = px.box(pd.concat([df_unit.assign(mode = "Unitaire"), df_batch.assign(mode="Batch")]), x = "mode", y = "ram", title = "RAM (%) : Unitaire vs Batch")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

        # Load
        fig = px.box(pd.concat([df_unit.assign(mode = "Unitaire"), df_batch.assign(mode = "Batch")]), x = "mode", y = "load", title = "Charge système : Unitaire vs Batch")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

        # Threads
        fig = px.box(pd.concat([df_unit.assign(mode = "Unitaire"), df_batch.assign(mode = "Batch")]), x = "mode", y = "threads", title = "Threads : Unitaire vs Batch")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)