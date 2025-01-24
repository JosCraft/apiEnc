from src.core.models.respuesta_domain import RespuestaDomain
from src.presentation.dto.respuesta_dto import RespuestaDto

def map_respuesta_domain_to_respuesta_dto(respuesta_dto: RespuestaDto) -> RespuestaDomain:
    return RespuestaDomain(
        id_encuesta=respuesta_dto.id_encuesta,
        id_pregunta=respuesta_dto.id_pregunta,
        id_opcion=respuesta_dto.id_opcion,
        respuesta_libre=respuesta_dto.respuesta_libre
    )
    