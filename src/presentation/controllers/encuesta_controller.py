from fastapi import APIRouter, Depends, HTTPException, status

from src.core.service.encuesta_service import EncuestaService
from src.core.dependency.dependency_inyection import build_encuesta_service

from src.presentation.dto.encuesta_dto import EncuestaDto
from src.presentation.mappers.map_encuesta_dto import map_encuesta_domain_to_encuesta_dto


encuesta_controller = APIRouter(prefix="/api/v1", tags=["Encuesta"])

@encuesta_controller.get("/encuesta")
async def get_encuestas(encuesta_service: EncuestaService = Depends(build_encuesta_service)):
    """
    Obtiene todas las encuestas de la base de datos.
    """
    encuestas = await encuesta_service.get_encuestas()
    return encuestas

@encuesta_controller.get("/encuesta/{id}")
async def get_encuesta_by_id(id: int, encuesta_service: EncuestaService = Depends(build_encuesta_service)):
    """
    Obtiene una encuesta específica por su ID.
    """
    encuesta = await encuesta_service.get_encuesta_by_id(id)
    if not encuesta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Encuesta no encontrada.")
    return encuesta

@encuesta_controller.post("/encuesta")
async def create_encuesta(encuesta: EncuestaDto, encuesta_service: EncuestaService = Depends(build_encuesta_service)):
    """
    Crea una nueva encuesta en la base de datos.
    """
    encuesta_id = await encuesta_service.create_encuesta(map_encuesta_domain_to_encuesta_dto(encuesta))
    return {"id": encuesta_id}