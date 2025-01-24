from src.core.abstracts.services.respuesta_service_abs import IRespuestaService
from src.core.abstracts.repository.respuesta_repository_abs import IRespuestaRepository

from src.core.models.respuesta_domain import RespuestaDomain

class RespuestaService(IRespuestaService):
    
    
    def __init__(self, respuesta_repository: IRespuestaRepository):
        self.respuesta_repository = respuesta_repository
    
    async def get_respuestas_by_pregunta(self, id_pregunta: int) -> list[RespuestaDomain]:
        return await self.respuesta_repository.get_respuestas_by_pregunta(id_pregunta)

    
    async def get_respuesta_by_id(self, id: int) -> RespuestaDomain:
        return await self.respuesta_repository.get_respuesta_by_id(id)
    
    
    async def create_respuesta(self, respuesta: RespuestaDomain):
        return await self.respuesta_repository.create_respuesta(respuesta)