import mysql.connector
from datetime import datetime

class Movimiento:
    def __init__(self, db_config):
        self.db_config = db_config

    def conectar_db(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            return connection
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            return None

    def registrar_movimiento(self, fecha, id_cuenta, referencia, id_consignacion=None, id_retiro=None, id_pagos=None):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = """
            INSERT INTO movimiento (fecha, id_cuenta, referencia, id_consignacion, id_retiro, id_pagos)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (fecha, id_cuenta, referencia, id_consignacion, id_retiro, id_pagos)
            cursor.execute(query, values)
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
