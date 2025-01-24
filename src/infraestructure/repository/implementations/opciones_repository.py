from src.core.abstracts.repository.opciones_repository_abs import IOpcionesRepository
from src.core.models.opciones_domain import OpcionesDomain
from psycopg2 import sql, Error


class OpcionesRepository(IOpcionesRepository):
    def __init__(self, connection):
        self.connection = connection

    async def get_opciones_by_pregunta(self, id_pregunta: int) -> list[OpcionesDomain]:
        """
        Obtiene todas las opciones asociadas a una pregunta por su ID.

        :param id_pregunta: ID de la pregunta.
        :return: Lista de OpcionesDomain.
        """
        list_opciones = []
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, id_pregunta, texto, codigo
                    FROM opciones 
                    WHERE id_pregunta = %s
                    """, 
                    (id_pregunta,)  # Tupla con un solo elemento
                )
                results = cursor.fetchall()
                if not results:
                    return []  # Si no hay resultados, devolvemos una lista vacía
                for result in results:
                    list_opciones.append(OpcionesDomain(
                        id=result[0],
                        id_pregunta=result[1],
                        texto=result[2],
                        codigo=result[3]
                    ))
                return list_opciones
        except Error as e:
            print(f"Error al obtener opciones por ID de pregunta: {e}")
            raise

    async def get_opcion_by_id(self, id: int) -> OpcionesDomain:
        """
        Obtiene una opción específica por su ID.

        :param id: ID de la opción.
        :return: Instancia de OpcionesDomain o None si no existe.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, id_pregunta, texto, codigo
                    FROM opciones 
                    WHERE id = %s
                    """, 
                    (id,)  # Tupla con un solo elemento
                )
                result = cursor.fetchone()
                if not result:
                    return None  # Si no hay resultados, devolvemos None
                return OpcionesDomain(
                    id=result[0],
                    id_pregunta=result[1],
                    texto=result[2],
                    codigo=result[3]
                )
        except Error as e:
            print(f"Error al obtener opción por ID: {e}")
            raise

    async def create_opcion(self, opcion: OpcionesDomain) -> bool:
        """
        Crea una nueva opción en la base de datos.

        :param opcion: Instancia de OpcionesDomain con los datos de la opción.
        :return: True si la creación fue exitosa, False en caso contrario.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO opciones (id_pregunta, texto, codigo) 
                    VALUES (%s, %s, %s)
                    """, 
                    (opcion.id_pregunta, opcion.texto, opcion.codigo)  
                )
                self.connection.commit()  # Confirmar la transacción
                return True
        except Error as e:
            print(f"Error al crear una opción: {e}")
            raise
