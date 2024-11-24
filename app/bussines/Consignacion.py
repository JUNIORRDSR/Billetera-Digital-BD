import mysql.connector

class Consignacion:
    def __init__(self, db_config):
        self.db_config = db_config

    def conectar_db(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            return connection
        except mysql.connector.Error as err:    
            print(f"Error al conectar a la base de datos: {err}")
            return None

    def verificar_cuenta(self, id_cuenta):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = "SELECT COUNT(*) FROM cuenta WHERE id_cuenta = %s"
            cursor.execute(query, (id_cuenta,))
            cuenta_existe = cursor.fetchone()[0] > 0
            cursor.close()
            connection.close()
            return cuenta_existe
        return False

    def obtener_saldo(self, id_cuenta):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = "SELECT saldo FROM cuenta WHERE id_cuenta = %s"
            cursor.execute(query, (id_cuenta,))
            saldo = cursor.fetchone()
            cursor.close()
            connection.close()
            return saldo[0] if saldo else 0
        return 0

    def registrar_consignacion(self, id_cuenta_origen, id_cuenta_destino, monto, descripcion, procedencia):
        if not self.verificar_cuenta(id_cuenta_destino):
            print("La cuenta de destino no existe.")
            return False

        saldo_origen = self.obtener_saldo(id_cuenta_origen)
        if monto > saldo_origen:
            print("El monto a consignar excede el saldo disponible en la cuenta de origen.")
            return False

        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = """
            INSERT INTO consignacion (id_cuenta_origen, id_cuenta_destino, monto, descripcion, procedencia)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (id_cuenta_origen, id_cuenta_destino, monto, descripcion, procedencia)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True
        return False

    def obtener_consignaciones(self, user_id):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = """
            SELECT c.id_consignacion, c.monto, c.descripcion, c.procedencia, cu_origen.numero_de_cuenta AS cuenta_origen, cu_destino.numero_de_cuenta AS cuenta_destino
            FROM consignacion c
            JOIN cuenta cu_origen ON c.id_cuenta_origen = cu_origen.id_cuenta
            JOIN cuenta cu_destino ON c.id_cuenta_destino = cu_destino.id_cuenta
            WHERE cu_origen.id_usuario = %s OR cu_destino.id_usuario = %s
            ORDER BY c.id_consignacion DESC;
            """
            cursor.execute(query, (user_id, user_id))
            consignaciones = cursor.fetchall()
            cursor.close()
            connection.close()
            return consignaciones
        return None
