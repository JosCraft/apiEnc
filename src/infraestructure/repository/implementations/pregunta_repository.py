from src.core.abstracts.repository.pregunta_repository_abs import IPreguntaRepository
from src.core.models.pregunta_domain import PreguntaDomain
from psycopg2 import sql, Error


class PreguntaRepository(IPreguntaRepository):
    def __init__(self, connection):
        self.connection = connection

    async def get_preguntas(self) -> list[PreguntaDomain]:
        """
        Obtiene todas las preguntas de la base de datos.

        :return: Lista de PreguntaDomain.
        """
        list_preguntas = []
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, texto, categoria
                    FROM preguntas
                    """
                )
                results = cursor.fetchall()
                if not results:
                    return []
                for result in results:
                    list_preguntas.append(PreguntaDomain(
                        id=result[0],
                        texto=result[1],
                        categoria=result[2]
                    ))
                return list_preguntas
        except Error as e:
            print(f"Error al obtener preguntas: {e}")
            raise

    async def get_pregunta_by_id(self, id: int) -> PreguntaDomain:
        """
        Obtiene una pregunta específica por su ID.

        :param id: ID de la pregunta.
        :return: Instancia de PreguntaDomain o None si no existe.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, texto, categoria
                    FROM preguntas 
                    WHERE id = %s
                    """, 
                    (id,)
                )
                result = cursor.fetchone()
                if not result:
                    return None
                return PreguntaDomain(
                    id=result[0],
                    texto=result[1],
                    categoria=result[2]
                )
        except Error as e:
            print(f"Error al obtener pregunta por ID: {e}")
            raise

    async def create_pregunta(self, pregunta: PreguntaDomain) -> int:
        """
        Crea una nueva pregunta en la base de datos.

        :param pregunta: Instancia de PreguntaDomain con los datos de la pregunta.
        :return: True si la creación fue exitosa, False en caso contrario.
        """
        print(f"Creando pregunta: {pregunta.texto}")
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO preguntas (texto, categoria) 
                    VALUES (%s, %s)
                    RETURNING id
                    """, 
                    (pregunta.texto, pregunta.categoria)
                )
                self.connection.commit()
                new_id = cursor.fetchone()[0]
                print(f"ID de la nueva pregunta: {new_id}")
                return new_id
        except Error as e:
            print(f"Error al crear una pregunta: {e}")
            raise
