from src.core.abstracts.repository.encuesta_repository_abs import IEncuestaRepository
from src.core.abstracts.services.encuesta_service_abs import IEncuestaService

from src.core.models.encuesta_domain import EncuestaDomain

class EncuestaService(IEncuestaService):
    
    def __init__(self, encuesta_repository: IEncuestaRepository):
        self.encuesta_repository = encuesta_repository
    
    async def get_encuestas(self) -> list[EncuestaDomain]:
        return await self.encuesta_repository.get_encuestas()
    
    async def get_encuesta_by_id(self, id: int) -> EncuestaDomain:
        return await self.encuesta_repository.get_encuesta_by_id(id)
    
    async def create_encuesta(self, encuesta: EncuestaDomain) -> int:
        return await self.encuesta_repository.create_encuesta(encuesta)