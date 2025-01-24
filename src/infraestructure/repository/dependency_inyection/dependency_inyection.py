from src.infraestructure.connection import get_connection


def get_db_connection():
    connection = get_connection()
    try:
        yield connection
    finally:
        connection.close()
