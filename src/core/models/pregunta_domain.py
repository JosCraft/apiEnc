from typing import Optional
from pydantic import BaseModel

class PreguntaDomain(BaseModel):
    id: Optional[int] = 0
    texto: str
    categoria: str