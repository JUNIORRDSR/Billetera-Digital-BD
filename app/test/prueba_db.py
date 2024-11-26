import os
import mysql.connector
from mysql.connector import Error

connection = None
def check_db_connection():
    
    try:
        # Configura tus credenciales de conexión
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),  # Por ejemplo, 'localhost'
            database=os.getenv("MYSQL_DATABASE"),  # Por ejemplo, 'my_database'
            user=os.getenv("MYSQL_USER"),  # Por ejemplo, 'root'
            password=os.getenv("MYSQL_PASSWORD")  # Por ejemplo, 'password'
        )

        if connection.is_connected():
            print("Conexión a la base de datos exitosa")
            db_info = connection.get_server_info()
            print("Versión del servidor MySQL:", db_info)

    except Error as e:
        print("Error al conectar a la base de datos:", e)

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    check_db_connection()
