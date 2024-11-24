import mysql.connector

class Pago:
    def __init__(self, db_config):
        self.db_config = db_config

    def conectar_db(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            return connection
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            return None

    def registrar_pago(self, costo_servicio, id_servicio):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = """
            INSERT INTO pagos (costo_servicio, id_servicio)
            VALUES (%s, %s)
            """
            values = (costo_servicio, id_servicio)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True
        return False

    def obtener_pagos(self, user_id):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = """
            SELECT p.id_pagos, p.costo_servicio, s.nombre_servicio
            FROM pagos p
            JOIN servicio s ON p.id_servicio = s.id_servicio
            WHERE p.id_usuario = %s
            ORDER BY p.id_pagos DESC;
            """
            cursor.execute(query, (user_id,))
            pagos = cursor.fetchall()
            cursor.close()
            connection.close()
            return pagos
        return None
