from flask import Flask
import os
import logging
import mysql.connector
from mysql.connector import Error
from app.bussines.Usuario import Usuario
from app.bussines.Pago import Pago
from app.bussines.Movimiento import Movimiento
from app.bussines.Consignacion import Consignacion
from app.bussines.Retiro import Retiro

# Configurar logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_url_path='/app/static/', static_folder='static')

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            database=os.getenv("MYSQL_DATABASE"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD")
        )
        if connection.is_connected():
            logger.info("Conexión a la base de datos exitosa")
            return connection
    except Error as e:
        logger.error(f"Error al conectar a la base de datos: {e}")
        return None

# Crear la conexión a la base de datos
db_connection = create_db_connection()

# Instanciar las clases de negocio
if db_connection:
    db = {
        'usuario': Usuario(db_connection),
        'pago': Pago(db_connection),
        'movimiento': Movimiento(db_connection),
        'consignacion': Consignacion(db_connection),
        'retiro': Retiro(db_connection)
    }
else:
    logger.error("No se pudo establecer la conexión a la base de datos. Las clases de negocio no se instanciarán.")

# Importar rutas después de definir db
from app.routes import *

logger.info("Aplicación inicializada correctamente")


