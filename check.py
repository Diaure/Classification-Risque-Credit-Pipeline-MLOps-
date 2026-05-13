import joblib

pipe = joblib.load("./BestModel/pipeline_complet.joblib")
pre = pipe.named_steps["preprocess"]

print("FEATURES ATTENDUES PAR LE PIPELINE :")
print(list(pre.transformers_[0][2]))  # les colonnes passées à 'num'
print("NOMBRE :", len(pre.transformers_[0][2]))
