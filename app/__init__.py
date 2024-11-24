from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
import os
import logging

# Configurar logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuración de la aplicación
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = os.environ.get('SECRET_KEY') or 'tu_clave_secreta'
    
    logger.info(f"Conectando a la base de datos: {Config.SQLALCHEMY_DATABASE_URI}")
    
    # Inicializar extensiones
    db = SQLAlchemy(app)
    ma = Marshmallow(app)

    # Importar rutas después de definir db
    from app.routes import *

    logger.info("Aplicación inicializada correctamente")

except Exception as e:
    logger.error(f"Error al inicializar la aplicación: {str(e)}")
    raise


