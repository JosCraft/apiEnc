from abc import ABC, abstractmethod

from src.core.models.encuesta_domain import EncuestaDomain

class IEncuestaService(ABC):
    
    @abstractmethod
    async def get_encuestas(self) -> list[EncuestaDomain]:
        pass
    
    @abstractmethod
    async def get_encuesta_by_id(self, id: int) -> EncuestaDomain:
        pass
    
    @abstractmethod
    async def create_encuesta(self, encuesta: EncuestaDomain) -> int:
        pass