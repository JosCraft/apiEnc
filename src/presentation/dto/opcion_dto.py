from dataclasses import dataclass

@dataclass
class OpcionDto:
    id_pregunta: int
    texto: str
    codigo: str