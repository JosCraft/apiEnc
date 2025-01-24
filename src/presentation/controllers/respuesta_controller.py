from fastapi import APIRouter, Depends, HTTPException, status
from src.core.service.respuesta_service import RespuestaService
from src.core.dependency.dependency_inyection import build_respuesta_service

from src.presentation.dto.respuesta_dto import RespuestaDto
from src.presentation.mappers.map_respuesta_dto import map_respuesta_domain_to_respuesta_dto

respuesta_controller = APIRouter(prefix="/api/v1", tags=["Respuesta"])

@respuesta_controller.get("/respuestas/{id_pregunta}")
async def get_respuestas(
    id_pregunta: int,
    respuesta_service: RespuestaService = Depends(build_respuesta_service)):
    """
    Obtiene todas las respuestas de la base de datos.
    """
    respuestas = await respuesta_service.get_respuestas_by_pregunta(id_pregunta)
    return respuestas

@respuesta_controller.get("/respuesta/{id}")
async def get_respuesta_by_id(id: int, respuesta_service: RespuestaService = Depends(build_respuesta_service)):
    """
    Obtiene una respuesta específica por su ID.
    """
    respuesta = await respuesta_service.get_respuesta_by_id(id)
    if not respuesta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Respuesta no encontrada.")
    return respuesta

@respuesta_controller.post("/respuesta")
async def create_respuesta(respuesta: RespuestaDto, respuesta_service: RespuestaService = Depends(build_respuesta_service)):
    """
    Crea una nueva respuesta en la base de datos.
    """
    
    return await respuesta_service.create_respuesta(map_respuesta_domain_to_respuesta_dto(respuesta))

