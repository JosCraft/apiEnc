from abc import ABC, abstractmethod

from src.core.models.respuesta_domain import RespuestaDomain

class IRespuestaService(ABC):
    
    @abstractmethod
    async def get_respuestas_by_pregunta(self, id_pregunta: int) -> list[RespuestaDomain]:
        pass
    
    @abstractmethod
    async def get_respuesta_by_id(self, id: int) -> RespuestaDomain:
        pass
    
    @abstractmethod
    async def create_respuesta(self, respuesta: RespuestaDomain):
        pass