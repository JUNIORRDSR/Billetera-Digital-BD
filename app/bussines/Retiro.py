import mysql.connector
import random

class Retiro:
    def __init__(self, db_config):
        self.db_config = db_config

    def conectar_db(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            return connection
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            return None

    def generar_codigo_retiro(self):
        return random.randint(100000, 999999)  # Genera un código de 6 dígitos

    def registrar_retiro(self, monto_retirar, id_ubicacion_retiro):
        codigo_retiro = self.generar_codigo_retiro()
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = """
            INSERT INTO retiro (monto_retirar, codigo_retiro, id_ubicacion_retiro)
            VALUES (%s, %s, %s)
            """
            values = (monto_retirar, codigo_retiro, id_ubicacion_retiro)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return codigo_retiro  # Devuelve el código generado
        return None

    def obtener_retiros(self, user_id):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = """
            SELECT r.id_retiro, r.monto_retirar, r.codigo_retiro, u.nombre, u.apellido
            FROM retiro r
            JOIN ubicacion u ON r.id_ubicacion_retiro = u.id
            WHERE u.id_usuario = %s
            ORDER BY r.id_retiro DESC;
            """
            cursor.execute(query, (user_id,))
            retiros = cursor.fetchall()
            cursor.close()
            connection.close()
            return retiros
        return None
