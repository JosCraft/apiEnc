from fastapi import APIRouter, Depends, HTTPException, status
from src.core.service.opciones_service import OpcionesService
from src.core.dependency.dependency_inyection import build_opciones_service

from src.presentation.dto.opcion_dto import OpcionDto
from src.presentation.mappers.map_opcion_dto import map_opcion_domain_to_opcion_dto

opciones_controller = APIRouter(prefix="/api/v1", tags=["Opciones"])

@opciones_controller.get("/opciones/{id_pregunta}")
async def get_opciones_by_pregunta(id_pregunta: int, opciones_service: OpcionesService = Depends(build_opciones_service)):
    """
    Obtiene todas las opciones asociadas a una pregunta por su ID.
    """
    opciones = await opciones_service.get_opciones_by_pregunta(id_pregunta)
    return opciones

@opciones_controller.get("/opcion/{id}")
async def get_opcion_by_id(id: int, opciones_service: OpcionesService = Depends(build_opciones_service)):
    """
    Obtiene una opción específica por su ID.
    """
    opcion = await opciones_service.get_opcion_by_id(id)
    if not opcion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Opción no encontrada.")
    return opcion

@opciones_controller.post("/opcion")    
async def create_opcion(opcion: OpcionDto, opciones_service: OpcionesService = Depends(build_opciones_service)):
    """
    Crea una nueva opción en la base de datos.
    """
    return await opciones_service.create_opcion(map_opcion_domain_to_opcion_dto(opcion))
    

