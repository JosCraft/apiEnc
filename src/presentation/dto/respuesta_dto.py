from dataclasses import dataclass
from typing import Optional
@dataclass
class RespuestaDto:
    id_encuesta: int
    id_pregunta: int
    id_opcion: Optional[int] = 0
    respuesta_libre: Optional[str] = ""