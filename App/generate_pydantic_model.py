import joblib
import numpy as np

df = joblib.load("./data/app_test_clean_v2.joblib")
example = df.sample(1).iloc[0].to_dict()
for k, v in example.items():
    if isinstance(v, float) and (np.isnan(v)):
        example[k] = None

fields = []

for col, dtype in df.dtypes.items():
    if dtype == bool or df[col].dropna().isin([0, 1, True, False]).all():
        py_type = "Optional[bool]"
    elif "int" in str(dtype):
        py_type = "Optional[int]"
    elif "float" in str(dtype):
        py_type = "Optional[float]"
    else:
        py_type = "Optional[str]"

    fields.append(f"    {col}: {py_type} = None")


model_code = f"""
from pydantic import BaseModel
from typing import Optional

class ClientFeatures(BaseModel):
{chr(10).join(fields)}
"""

with open("App/models.py", "w") as f:
    f.write(model_code)

print("✔️ Modèle Pydantic généré dans App/models.py")
