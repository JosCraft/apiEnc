from src.core.models.encuesta_domain import EncuestaDomain

from src.presentation.dto.encuesta_dto import EncuestaDto

def map_encuesta_domain_to_encuesta_dto(encuesta_dto:EncuestaDto) -> EncuestaDomain:
    return EncuestaDomain(
        fecha=encuesta_dto.fecha
    )