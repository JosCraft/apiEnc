import psycopg2
from psycopg2 import pool, OperationalError

try:
    connection_pool = pool.SimpleConnectionPool(
        1,  
        5,  
        user='kriakthar',
        password='RbdV7z2jV1h338rGNR7eTuTG70zRwdZY',
        host='dpg-cu9ppkrqf0us73c3e2g0-a.oregon-postgres.render.com',
        port='5432',  
        database='encuestra'
    )
    print("Pool de conexiones creado exitosamente.")

except OperationalError as e:
    print(f"Error creando el pool de conexiones: {e}")

def get_connection():
    try:
        connection = connection_pool.getconn()  
        print("Conexión obtenida del pool.")
        return connection
    except OperationalError as e:
        print(f"Error al obtener la conexión del pool: {e}")
        return None


def release_connection(connection):
    try:
        connection_pool.putconn(connection)  
        print("Conexión devuelta al pool.")
    except OperationalError as e:
        print(f"Error al liberar la conexión: {e}")


def close_pool():
    try:
        connection_pool.closeall()  
        print("Todas las conexiones en el pool han sido cerradas.")
    except OperationalError as e:
        print(f"Error al cerrar el pool de conexiones: {e}")
