import mysql.connector
import os
import logging
from flask import session
logger = logging.getLogger(__name__)

class Consignacion:
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

    def verificar_cuenta(self, telefono_destino):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = "SELECT COUNT(*) FROM usuario WHERE telefono= %s"
            cursor.execute(query, (telefono_destino,))
            cuenta_existe = cursor.fetchone()[0] > 0
            cursor.close()
            connection.close()
            return cuenta_existe
        return False

    def obtener_saldo(self, telefono_origen):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = "SELECT saldo FROM cuenta WHERE id_usuario = (SELECT id_usuario FROM usuario WHERE telefono = %s LIMIT 1)"
            cursor.execute(query, (telefono_origen,))
            saldo = cursor.fetchone()
            cursor.close()
            connection.close()
            return saldo[0] if saldo else 0
        return 0

    def registrar_consignacion(self, telefono_origen, telefono_destino, monto, descripcion, procedencia):
        if not self.verificar_cuenta(telefono_destino):
            return {'success': False, 'message': "La cuenta de destino no existe."}

        # Obtener el saldo de la base de datos usando el teléfono de origen
        saldo_origen = self.obtener_saldo(telefono_origen)  # Cambiado para obtener el saldo de la base de datos
        if saldo_origen is None:
            return {'success': False, 'message': "No se pudo obtener el saldo de la cuenta de origen."}

        if monto > saldo_origen:
            return {'success': False, 'message': "El monto a consignar excede el saldo disponible en la cuenta de origen."}

        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            try:
                # Insertar la consignación
                query = """
                INSERT INTO consignacion (telefono_origen, telefono_destino, monto, descripcion, procedencia)
                VALUES (%s, %s, %s, %s, %s)
                """
                values = (telefono_origen, telefono_destino, monto, descripcion, procedencia)
                cursor.execute(query, values)

                try:
                    # Restar el monto del saldo del usuario de origen
                    query_restar = """
                    UPDATE cuenta 
                    SET saldo = saldo - %s 
                    WHERE id_usuario = (SELECT u.id_usuario FROM usuario as u WHERE u.telefono = %s)
                    """
                    cursor.execute(query_restar, (monto, telefono_origen))

                except mysql.connector.Error as e:
                    connection.rollback()  # Revertir cambios en caso de error
                    return {'success': False, 'message': f"Error al restar el monto del saldo del usuario de origen: {str(e)}"}

                try:
                    # Sumar el monto al saldo del usuario de destino
                    query_sumar = """
                    UPDATE cuenta 
                    SET saldo = saldo + %s 
                    WHERE id_usuario = (SELECT u.id_usuario FROM usuario as u WHERE u.telefono = %s)
                    """
                    cursor.execute(query_sumar, (monto, telefono_destino))

                except mysql.connector.Error as e:
                    connection.rollback()  # Revertir cambios en caso de error
                    return {'success': False, 'message': f"Error al sumar el monto al saldo del usuario de destino: {str(e)}"}

                connection.commit()
                return {'success': True, 'message': "Transacción registrada con éxito."}  # Retornar éxito si se registra correctamente
            except Exception as e:
                connection.rollback()  # Revertir cambios en caso de error
                return {'success': False, 'message': f"Error al procesar la transacción: {str(e)}"}  # Retornar mensaje de error
            finally:
                cursor.close()
                connection.close()
        return {'success': False, 'message': "Error al conectar a la base de datos."}

    def obtener_consignaciones(self, user_id):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = """
            SELECT c.id_consignacion, c.monto, c.descripcion, c.procedencia, cu_origen.numero_de_cuenta AS cuenta_origen, cu_destino.numero_de_cuenta AS cuenta_destino
            FROM consignacion c
            JOIN cuenta cu_origen ON c.telefono_origen = cu_origen.id_cuenta
            JOIN cuenta cu_destino ON c.telefono_destino = cu_destino.id_cuenta
            WHERE cu_origen.id_usuario = %s OR cu_destino.id_usuario = %s
            ORDER BY c.id_consignacion DESC;
            """
            cursor.execute(query, (user_id, user_id))
            consignaciones = cursor.fetchall()
            cursor.close()
            connection.close()
            return consignaciones
        return None
