import mysql.connector

class Usuario:
    def __init__(self, db_config):
        self.db_config = db_config

    def conectar_db(self):
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            return self.connection
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            return None

    def registrar_usuario(self, tipo_de_id, nombre, apellido, numero_documento, telefono, correo, fecha_nacimiento):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            
            # Verificar si el usuario ya existe
            query_verificacion = """
            SELECT * FROM usuario WHERE telefono = %s OR correo = %s OR numero_documento = %s
            """
            cursor.execute(query_verificacion, (telefono, correo, numero_documento))
            if cursor.fetchone():  # Si se encuentra un registro, el usuario ya existe
                cursor.close()
                connection.close()
                return False  # Retornar False si el usuario ya existe

            query = """
            INSERT INTO usuario (tipo_de_id, nombre, apellido, numero_documento, telefono, correo, fecha_nacimiento)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (tipo_de_id, nombre, apellido, numero_documento, telefono, correo, fecha_nacimiento)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True
        return False

    def iniciar_sesion(self, tipo_de_id, numero_documento, contraseña):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM usuarios WHERE tipo_de_id = %s AND numero_documento = %s AND contraseña = %s"
            cursor.execute(query, (tipo_de_id, numero_documento, contraseña))
            usuario = cursor.fetchone()
            cursor.close()
            connection.close()
            return usuario
        return None

    def obtener_informacion_usuario(self, id_numero):
        connection = self.conectar_db()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM usuarios WHERE id_numero = %s"
            cursor.execute(query, (id_numero,))
            usuario = cursor.fetchone()
            cursor.close()
            connection.close()
            return usuario
        return None
