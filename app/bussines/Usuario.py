import mysql.connector
import random

class Usuario:
    def __init__(self, db_connection):
        self.connection = db_connection

    def generar_numero_cuenta(self):
        # Generar un número de cuenta aleatorio (puedes ajustar la lógica según tus necesidades)
        return f"CU{random.randint(10000000, 99999999)}"  # Ejemplo: CU12345678

    def registrar_usuario(self, tipo_de_id, nombre, apellido, numero_documento, telefono, correo, fecha_nacimiento, contraseña):
        if self.connection:
            cursor = self.connection.cursor()
            
            # Verificar si el usuario ya existe
            query_verificacion = """
            SELECT * FROM usuario WHERE telefono = %s OR correo = %s OR numero_documento = %s
            """
            cursor.execute(query_verificacion, (telefono, correo, numero_documento))
            if cursor.fetchone():  # Si se encuentra un registro, el usuario ya existe
                cursor.close()
                return False  # Retornar False si el usuario ya existe

            # Generar un número de cuenta aleatorio
            numero_de_cuenta = self.generar_numero_cuenta()

            # Insertar el nuevo usuario
            query = """
            INSERT INTO usuario (tipo_de_id, nombre, apellido, numero_documento, telefono, correo, fecha_nacimiento, contraseña)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (tipo_de_id, nombre, apellido, numero_documento, telefono, correo, fecha_nacimiento, contraseña)
            cursor.execute(query, values)
            self.connection.commit()

            # Obtener el ID del nuevo usuario
            usuario_id = cursor.lastrowid

            # Insertar la cuenta con el número de cuenta y saldo inicial
            query_cuenta = """
            INSERT INTO cuentas (id_usuario, numero_de_cuenta, saldo)
            VALUES (%s, %s, %s)
            """
            cursor.execute(query_cuenta, (usuario_id, numero_de_cuenta, 0))  # saldo inicial en 0
            self.connection.commit()

            cursor.close()
            return True
        return False

    def iniciar_sesion(self, tipo_de_id, numero_documento, contraseña):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                query = "SELECT * FROM usuario WHERE tipo_de_id = %s AND numero_documento = %s AND contraseña = %s"
                cursor.execute(query, (tipo_de_id, numero_documento, contraseña))
                usuario = cursor.fetchone()
                return usuario
            except Exception as e:
                # Manejar el error (puedes registrar el error o lanzar una excepción)
                print(f"Error al iniciar sesión: {str(e)}")
                return None
            finally:
                cursor.close()  # Asegurarse de cerrar el cursor
        return None

    def obtener_informacion_usuario(self, id_numero):
        if self.connection:
            cursor = self.connection.cursor()
            query = "SELECT * FROM usuario WHERE id_numero = %s"
            cursor.execute(query, (id_numero,))
            usuario = cursor.fetchone()
            cursor.close()
            return usuario
        return None
