import joblib
import numpy as np
import re

df = joblib.load("./data/app_test_clean_v2.joblib")

def sanitize(name: str) -> str:
    """
    Transforme un nom de colonne en identifiant Python valide.
    """
    # Remplacer tout caractère non alphanumérique par un underscore
    name = re.sub(r'[^0-9a-zA-Z_]', '_', name)

    # Si le nom commence par un chiffre → préfixer
    if re.match(r'^[0-9]', name):
        name = f"col_{name}"

    return name


example = df.sample(1).iloc[0].to_dict()
for k, v in example.items():
    if isinstance(v, float) and (np.isnan(v)):
        example[k] = None

fields = []

for col, dtype in df.dtypes.items():
    clean_col = sanitize(col)

    if dtype == bool or df[col].dropna().isin([0, 1, True, False]).all():
        py_type = "Optional[bool]"
    elif "int" in str(dtype):
        py_type = "Optional[int]"
    elif "float" in str(dtype):
        py_type = "Optional[float]"
    else:
        py_type = "Optional[str]"

    fields.append(f"    {clean_col}: {py_type} = None")


model_code = f"""
from pydantic import BaseModel
from typing import Optional

class ClientFeatures(BaseModel):
{chr(10).join(fields)}
"""

with open("App/models.py", "w") as f:
    f.write(model_code)

print("✔️ Modèle Pydantic généré dans App/models.py")
