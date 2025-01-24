from src.core.abstracts.repository.pregunta_repository_abs import IPreguntaRepository
from src.core.abstracts.services.pregunta_service_abs import IPreguntaService

from src.core.models.pregunta_domain import PreguntaDomain

class PreguntaService(IPreguntaService):
    
    def __init__(self, pregunta_repository: IPreguntaRepository):
        self.pregunta_repository = pregunta_repository
    
    async def get_preguntas(self) -> list[PreguntaDomain]:
        return await self.pregunta_repository.get_preguntas()
    
    async def get_pregunta_by_id(self, id: int) -> PreguntaDomain:
        return await self.pregunta_repository.get_pregunta_by_id(id)
    
    async def create_pregunta(self, pregunta: PreguntaDomain)->int:
        return await self.pregunta_repository.create_pregunta(pregunta)