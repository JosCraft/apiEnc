from src.core.models.opciones_domain import OpcionesDomain
from src.presentation.dto.opcion_dto import OpcionDto

def map_opcion_domain_to_opcion_dto(opciondto: OpcionDto) -> OpcionesDomain:
    return OpcionesDomain(
        id_pregunta=opciondto.id_pregunta,
        texto=opciondto.texto,
        codigo=opciondto.codigo
    )
