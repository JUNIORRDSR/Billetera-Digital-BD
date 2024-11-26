import mysql.connector
from datetime import datetime
import logging
from flask import session
import os

logger = logging.getLogger(__name__)
class Movimiento:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None  # Inicializa la conexión como None

    def verificar_conexion(self):
        """Verifica si la conexión a la base de datos está activa."""
        if self.connection is None or not self.connection.is_connected():
            try:
                self.connection = mysql.connector.connect(
                    host=os.getenv("MYSQL_HOST"),
                    database=os.getenv("MYSQL_DATABASE"),
                    user=os.getenv("MYSQL_USER"),
                    password=os.getenv("MYSQL_PASSWORD")
                )
                logger.info("Conexión a la base de datos restablecida.")
            except mysql.connector.Error as e:
                logger.error(f"Error al intentar reconectar a la base de datos: {str(e)}")
                return False
        return True

    def conectar_db(self):
        """Conecta a la base de datos utilizando la configuración proporcionada."""
        if not self.verificar_conexion():  # Verifica la conexión antes de intentar conectarse
            return None
        return self.connection  # Devuelve la conexión activa

    def registrar_movimiento(self, fecha, id_cuenta, referencia, id_consignacion=None, id_retiro=None, id_pagos=None):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = """
            INSERT INTO movimiento (fecha, id_cuenta, referencia, id_consignacion, id_retiro, id_pagos)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (fecha, id_cuenta, referencia, id_consignacion, id_retiro, id_pagos)
            cursor.execute(query, (values))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        return False

    def obtener_movimientos_usuario(self, user_id):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = """
            SELECT 
                m.fecha AS Fecha,
                CONCAT(u.nombre, ' ', u.apellido) AS Usuario,
                c.numero_de_cuenta AS Cuenta,
                CASE 
                    WHEN m.id_consignacion IS NOT NULL THEN 'Consignación'
                    WHEN m.id_retiro IS NOT NULL THEN 'Retiro'
                    WHEN m.id_pagos IS NOT NULL THEN 'Pago'
                    ELSE 'Otro'
                END AS TipoMovimiento,
                COALESCE(cs.monto, r.monto_retirar, p.costo_servicio) AS Monto,
                m.referencia AS Referencia
            FROM movimiento m
            JOIN cuenta c ON m.id_cuenta = c.id_cuenta
            JOIN usuario u ON c.id_usuario = u.id_usuario
            LEFT JOIN consignacion cs ON m.id_consignacion = cs.id_consignacion
            LEFT JOIN retiro r ON m.id_retiro = r.id_retiro
            LEFT JOIN pagos p ON m.id_pagos = p.id_pagos
            WHERE u.id_usuario = %s
            ORDER BY m.fecha DESC;
            """
            cursor.execute(query, (user_id,))
            movimientos = cursor.fetchall()
            cursor.close()
            connection.close()
            return movimientos
        return None
