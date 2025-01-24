from pydantic import BaseModel
from typing import Optional

class OpcionesDomain(BaseModel):
    id: Optional[int] = 0
    id_pregunta: int
    texto: str
    codigo: str