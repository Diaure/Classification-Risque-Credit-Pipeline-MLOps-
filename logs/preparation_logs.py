import json
import pandas as pd
from pathlib import Path

log_file = Path("logs/predictions_log.jsonl")
output_parquet = Path("logs/predictions_log.parquet")

def load_jsonl(path): # fonction qui va lire le fichier jsonl ligne par ligne et retourner une liste de dictionnaires
    rows = []
    with path.open() as f:
        for line in f:
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows

def prepare_logs(): # si aucun fichier trouvé renvoyer un message
    if not log_file.exists():
        print("Aucun fichier de logs trouvé.")
        return

    # Suivi du processus de lecture des lignes du fichier et de séparation des différente logs métier(input, outputs), et opérationnels (latence, temps, etc)
    rows = load_jsonl(log_file)
    df = pd.DataFrame(rows)

    # Logs métier contenant "inputs"
    df_model = df[df["inputs"].notna()].copy()

    # Les autres logs
    df_ops = df[df["inputs"].isna()].copy()

    print(f"{len(df_model)} logs modèle")
    print(f"{len(df_ops)} logs opérationnels")

    # Extraction des features (inputs)
    df_inputs = df_model["inputs"].apply(pd.Series)

    # Extraction des outputs
    df_outputs = df_model[["score", "decision", "threshold"]]

    # Fusion
    df_final = pd.concat([df_inputs, df_outputs], axis=1)

    # Ajout du timestamp
    df_final["timestamp"] = df_model["timestamp"].values

    # Ajout du request_id
    df_final["request_id"] = df_model["request_id"].values

    # Ajout de la latence (join avec df_ops)
    df_ops_clean = df_ops.drop(columns=["inputs"], errors="ignore")
    # df_ops_small = df_ops[["request_id", "latency_ms"]]
    # df_final = df_final.merge(df_ops_small, how="left", left_index=True, right_index=True)

    # Merge complet avec les logs opérationnels
    # df_ops_full = df_ops.drop(columns=["inputs"], errors="ignore")
    df_final = df_final.merge(df_ops_clean, how="left", on="request_id")
    
    df_final.to_parquet(output_parquet, index=False)
    print(f"Fichier généré : {output_parquet}")

if __name__ == "__main__":
    prepare_logs()
