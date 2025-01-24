from abc import ABC, abstractmethod

from src.core.models.opciones_domain import OpcionesDomain

class IOpcionesRepository(ABC):
    
    @abstractmethod
    async def get_opciones_by_pregunta(self, id_pregunta: int) -> list[OpcionesDomain]:
        pass
    
    @abstractmethod
    async def get_opcion_by_id(self, id: int) -> OpcionesDomain:
        pass
    
    @abstractmethod
    async def create_opcion(self, opcion: OpcionesDomain):
        pass