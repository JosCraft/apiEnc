from abc import ABC, abstractmethod

from src.core.models.pregunta_domain import PreguntaDomain

class IPreguntaService(ABC):
    
    @abstractmethod
    async def get_preguntas(self) -> list[PreguntaDomain]:
        pass
    
    @abstractmethod
    async def get_pregunta_by_id(self, id: int) -> PreguntaDomain:
        pass
    
    @abstractmethod
    async def create_pregunta(self, pregunta: PreguntaDomain)->int:
        pass