from src.core.abstracts.repository.encuesta_repository_abs import IEncuestaRepository
from src.core.models.encuesta_domain import EncuestaDomain
from psycopg2 import sql, Error


class EncuestaRepository(IEncuestaRepository):
    def __init__(self, connection):
        self.connection = connection

    async def get_encuestas(self) -> list[EncuestaDomain]:
        """
        Obtiene todas las encuestas de la base de datos.

        :return: Lista de EncuestaDomain.
        """
        list_encuestas = []
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, fecha 
                    FROM encuestas
                    """
                )
                results = cursor.fetchall()
                if not results:
                    return []
                for result in results:
                    list_encuestas.append(EncuestaDomain(
                        id=result[0],
                        fecha=result[1]
                    ))
                return list_encuestas
        except Error as e:
            print(f"Error al obtener encuestas: {e}")
            raise

    async def get_encuesta_by_id(self, id: int) -> EncuestaDomain:
        """
        Obtiene una encuesta específica por su ID.

        :param id: ID de la encuesta.
        :return: Instancia de EncuestaDomain o None si no existe.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, fecha 
                    FROM encuestas 
                    WHERE id = %s
                    """,
                    (id,)
                )
                result = cursor.fetchone()
                if not result:
                    return None
                return EncuestaDomain(id=result[0], fecha=result[1])
        except Error as e:
            print(f"Error al obtener encuesta por ID: {e}")
            raise

    async def create_encuesta(self, encuesta: EncuestaDomain) -> int:
        """
        Crea una nueva encuesta en la base de datos.

        :param encuesta: Instancia de EncuestaDomain con los datos de la encuesta.
        :return: ID de la encuesta creada.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO encuestas (fecha) 
                    VALUES (%s) 
                    RETURNING id
                    """,
                    (encuesta.fecha,)
                )
                self.connection.commit()
                new_id = cursor.fetchone()[0]
                return new_id
        except Error as e:
            print(f"Error al crear una encuesta: {e}")
            raise
