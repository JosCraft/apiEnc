from src.core.models.pregunta_domain import PreguntaDomain
from src.presentation.dto.pregunta_dto import PreguntaDto

def map_pregunta_domain_to_pregunta_dto(pregunta_dto: PreguntaDto) -> PreguntaDomain:
    return PreguntaDomain(
        texto=pregunta_dto.texto,
        categoria=pregunta_dto.categoria
    )
    