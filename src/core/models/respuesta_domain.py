from pydantic import BaseModel
from typing import Optional

class RespuestaDomain(BaseModel):
    id: Optional[int] = 0
    id_encuesta: int
    id_pregunta: int
    id_opcion: Optional[int] = 0
    respuesta_libre: Optional[str] = ""