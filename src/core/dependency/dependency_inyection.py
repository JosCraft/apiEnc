
from fastapi import Depends

from src.core.service.encuesta_service import EncuestaService
from src.core.service.opciones_service import OpcionesService
from src.core.service.pregunta_service import PreguntaService
from src.core.service.respuesta_service import RespuestaService

from src.infraestructure.repository.dependency_inyection.dependency_inyection import get_db_connection

from src.infraestructure.repository.implementations.encuesta_repository import EncuestaRepository
from src.infraestructure.repository.implementations.opciones_repository import OpcionesRepository
from src.infraestructure.repository.implementations.pregunta_repository import PreguntaRepository
from src.infraestructure.repository.implementations.respuesta_repository import RespuestaRepository


def build_encuesta_service(
    db_connection=Depends(get_db_connection)
):
    return EncuestaService(EncuestaRepository(db_connection))

def build_opciones_service(
    db_connection=Depends(get_db_connection)
):
    return OpcionesService(OpcionesRepository(db_connection))   

def build_pregunta_service(
    db_connection=Depends(get_db_connection)
):
    return PreguntaService(PreguntaRepository(db_connection))

def build_respuesta_service(
    db_connection=Depends(get_db_connection)
):
    return RespuestaService(RespuestaRepository(db_connection))


