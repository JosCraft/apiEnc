from src.core.abstracts.services.opciones_service_abs import IOpcionesService
from src.core.abstracts.repository.opciones_repository_abs import IOpcionesRepository

from src.core.models.opciones_domain import OpcionesDomain

class OpcionesService(IOpcionesService):
    
    def __init__(self, opciones_repository: IOpcionesRepository):
        self.opciones_repository = opciones_repository
    
    async def get_opciones_by_pregunta(self, id_pregunta: int) -> list[OpcionesDomain]:
        return await self.opciones_repository.get_opciones_by_pregunta(id_pregunta)
    
    async def get_opcion_by_id(self, id: int) -> OpcionesDomain:
        return await self.opciones_repository.get_opcion_by_id(id)
    
    async def create_opcion(self, opcion: OpcionesDomain):
        return await self.opciones_repository.create_opcion(opcion)