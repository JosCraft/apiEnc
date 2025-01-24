from fastapi import APIRouter, Depends, HTTPException, status
from src.core.abstracts.services.pregunta_service_abs import IPreguntaService
from src.core.dependency.dependency_inyection import build_pregunta_service

from src.presentation.dto.pregunta_dto import PreguntaDto
from src.presentation.mappers.map_pregunta_dto import map_pregunta_domain_to_pregunta_dto

pregunta_controller = APIRouter(prefix="/api/v1", tags=["Pregunta"])

@pregunta_controller.get("/preguntas")
async def get_preguntas(pregunta_service: IPreguntaService = Depends(build_pregunta_service)):
    """
    Obtiene todas las preguntas de la base de datos.
    """
    preguntas = await pregunta_service.get_preguntas()
    return preguntas

@pregunta_controller.get("/pregunta/{id}")
async def get_pregunta_by_id(id: int, pregunta_service: IPreguntaService = Depends(build_pregunta_service)):
    """
    Obtiene una pregunta específica por su ID.
    """
    pregunta = await pregunta_service.get_pregunta_by_id(id)
    if not pregunta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pregunta no encontrada.")
    return pregunta

@pregunta_controller.post("/pregunta")
async def create_pregunta(pregunta: PreguntaDto, pregunta_service: IPreguntaService = Depends(build_pregunta_service)):
    """
    Crea una nueva pregunta en la base de datos.
    """
    pregunta_id = await  pregunta_service.create_pregunta(map_pregunta_domain_to_pregunta_dto(pregunta))
    return {"id": pregunta_id}
    
