from pydantic import BaseModel
from typing import Optional

class ClientFeatures(BaseModel):
    SK_ID_CURR: Optional[int] = None
    AGE: Optional[int] = None
    INCOME: Optional[float] = None

# Créer le modèle Pydantic
# ClientFeatures = create_model("ClientFeatures", **fields)
# ClientFeatures.model_config = {
#     "json_schema_extra": {
#         "example": example}}