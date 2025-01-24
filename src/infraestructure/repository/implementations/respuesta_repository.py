from src.core.abstracts.repository.respuesta_repository_abs import IRespuestaRepository
from src.core.models.respuesta_domain import RespuestaDomain
from psycopg2 import sql, Error


class RespuestaRepository(IRespuestaRepository):
    def __init__(self, connection):
        self.connection = connection

    async def get_respuestas_by_pregunta(self, id_pregunta: int) -> list[RespuestaDomain]:
        """
        Obtiene todas las respuestas asociadas a una pregunta por su ID.

        :param id_pregunta: ID de la pregunta.
        :return: Lista de RespuestaDomain.
        """
        list_respuestas = []
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, id_encuesta, id_pregunta ,id_opcion, respuesta_libre
                    FROM respuestas 
                    WHERE id_pregunta = %s
                    """, 
                    (id_pregunta,)
                )
                results = cursor.fetchall()
                if not results:
                    return []
                for result in results:
                    list_respuestas.append(RespuestaDomain(
                        id=result[0],
                        id_encuesta=result[1],
                        id_pregunta=result[2],
                        id_opcion=result[3],
                        respuesta_libre=result[4]
                    ))
                return list_respuestas
        except Error as e:
            print(f"Error al obtener respuestas por ID de pregunta: {e}")
            raise

    async def get_respuesta_by_id(self, id: int) -> RespuestaDomain:
        """
        Obtiene una respuesta específica por su ID.

        :param id: ID de la respuesta.
        :return: Instancia de RespuestaDomain o None si no existe.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, id_encuesta, id_pregunta, id_opcion, respuesta_libre
                    FROM respuestas 
                    WHERE id = %s
                    """, 
                    (id,)
                )
                result = cursor.fetchone()
                if not result:
                    return None
                return RespuestaDomain(**result)
        except Error as e:
            print(f"Error al obtener respuesta por ID: {e}")
            raise

    async def create_respuesta(self, respuesta: RespuestaDomain) -> bool:
        """
        Crea una nueva respuesta en la base de datos.

        :param respuesta: Instancia de RespuestaDomain con los datos de la respuesta.
        :return: True si la creación fue exitosa, False en caso contrario.
        """
        print(respuesta)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO respuestas (id_encuesta, id_pregunta, id_opcion, respuesta_libre) 
                    VALUES (%s, %s, %s, %s)
                    """, 
                    (respuesta.id_encuesta, respuesta.id_pregunta, respuesta.id_opcion, respuesta.respuesta_libre)
                )
                self.connection.commit()
                return True
        except Error as e:
            print(f"Error al crear una respuesta: {e}")
            raise
