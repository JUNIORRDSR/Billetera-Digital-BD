from flask import render_template, request, redirect, jsonify, session  # Importar el módulo de sesión de Flask
from app import app,db_connection as db
from app.bussines.Consignacion import Consignacion
from app.bussines.Usuario import Usuario


# Rutas de páginas principales
@app.route('/app/templates/index.html')
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


# ruta para la página de inicio

@app.route('/app/templates/pages/inicio.html')
def inicio():
    return render_template('pages/inicio.html')  # Pasa el saldo a la plantilla

# ruta para la página de login
@app.route('/app/templates/pages/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()  # Obtener los datos en formato JSON
        
        # Verificar que las claves existen en el JSON
        try:
            tipo_de_id = data['id-type']
            numero_documento = data['id-number']
            contraseña = data['password']
            
            # Print the received data
            print(f"Tipo de ID: {tipo_de_id}")
            print(f"Numero de Documento: {numero_documento}")
            print(f"Contraseña: {contraseña}")
        except KeyError as e:
            return {'error': f'Falta el campo: {str(e)}'}, 400  # Retornar un error si falta un campo
        
        usuario = Usuario(db)
        usuario_logueado = usuario.iniciar_sesion(tipo_de_id, numero_documento, contraseña)
        if usuario_logueado:
            session['id_usuario'] = usuario_logueado[0]  # Almacenar ID de usuario
            session['telefono_usuario'] = usuario_logueado[5]  # Almacenar número de teléfono (asegúrate de que el índice sea correcto)
            return {'message': 'Inicio de sesión exitoso'}, 200  # Devolver un mensaje de éxito
        else:
            return {'error': 'Credenciales incorrectas'}, 401  # Devolver un mensaje de error

    return render_template('pages/login.html')




# ruta para la página de registro
@app.route('/app/templates/pages/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()  # Obtener los datos en formato JSON
        
        # Verificar que las claves existen en el JSON
        try:
            tipo_de_id = data['id-type']
            nombre = data['first-name']
            apellido = data['last-name']
            numero_documento = data['id-number']
            telefono = data['phone']
            correo = data['email']
            fecha_nacimiento = data['birthdate']
            contraseña = data['password']
            
            # Print the received data
            print(f"Tipo de ID: {tipo_de_id}")
            print(f"Nombre: {nombre}")
            print(f"Apellido: {apellido}")
            print(f"Numero de Documento: {numero_documento}")
            print(f"Telefono: {telefono}")
            print(f"Correo: {correo}")
            print(f"Fecha de Nacimiento: {fecha_nacimiento}")
            print(f"Contraseña: {contraseña}")
        except KeyError as e:
            return {'error': f'Falta el campo: {str(e)}'}, 400  # Retornar un error si falta un campo
        
        usuario = Usuario(db)
        if not usuario.registrar_usuario(tipo_de_id, nombre, apellido, numero_documento, telefono, correo, fecha_nacimiento, contraseña):
            return {'error': 'Error al registrar el usuario'}, 500  # Manejo de error
        return {'message': 'Registro exitoso'}, 200
    return render_template('pages/register.html')




# ruta para la página de retiros
@app.route('/app/templates/pages/retiros.html')
def retiros():
    return render_template('pages/retiros.html')

# ruta para la página de transferencias
@app.route('/app/templates/pages/transferencias.html', methods=['GET', 'POST', 'PUT'])
def registrar_transaccion():
    
    if request.method == 'POST':
        # Obtener el número de teléfono de la cuenta de origen desde la sesión
        telefono_origen = session.get('telefono_usuario')  # Cambiado para obtener el teléfono
        print(f"Número de teléfono almacenado en la sesión: {telefono_origen}")
        if telefono_origen is None:
            return jsonify({'error': 'Número de teléfono de la cuenta de origen no disponible en la sesión'}), 400

        # Obtener los datos del formulario
        data = request.get_json()  # Cambiar a request.get_json() para recibir datos JSON
        if not data:
            return jsonify({'error': 'No se recibieron datos JSON'}), 400  # Manejo de error si no se reciben datos

        # Verificar que las claves existen en el JSON
        telefono_destino = data['cuentaDestino']
        monto = data['monto']
        descripcion = data.get('descripcion', '')  # Descripción opcional

        # Crear una instancia de Consignacion y registrar la transacción
        consignacion = Consignacion(db)
        resultado = consignacion.registrar_consignacion(telefono_origen, telefono_destino, monto, descripcion, procedencia='EasyPay')
        if resultado['success']:
            return jsonify({'message': resultado['message']}), 200  # Respuesta exitosa
        else:
            return jsonify({'error': resultado['message']}), 500  # Manejo de error

    # Si es un método GET, simplemente renderiza la página de transferencias
    return render_template('pages/transferencias.html')

# ruta para la página de pagos
@app.route('/app/templates/pages/pagos.html')
def pagos():
    return render_template('pages/pagos.html')

# Rutas de páginas de Movimientos
@app.route('/app/templates/pages/movimientos.html')
def movimientos():
    return render_template('pages/movimientos.html')

# Rutas de páginas de Consignaciones
@app.route('/app/templates/pages/consignaciones.html')
def consignaciones():
    return render_template('pages/consignaciones.html')

# Rutas de páginas de Configuración
@app.route('/app/templates/pages/configuracion.html')
def configuracion():
    return render_template('pages/configuracion.html')

@app.route('/api/saldo')  # Nueva ruta para obtener el saldo en formato JSON
def obtener_saldo():
    telefono_origen = session.get('telefono_usuario')  # Obtener el teléfono del usuario
    print(f"Número de teléfono almacenado en la sesión: {telefono_origen}")
    
    if telefono_origen is None:
        return jsonify({'error': 'Número de teléfono de la cuenta de origen no disponible en la sesión'}), 400
    
    consignacion = Consignacion(db)
    
    try:
        saldo = consignacion.obtener_saldo(telefono_origen)
        print(f"Saldo de la cuenta de origen: {saldo}")
    except Exception as e:
        return jsonify({'error': f'Error al obtener el saldo: {str(e)}'}), 500  # Manejo de error

    return jsonify({'saldo': saldo})  # Devuelve el saldo como JSON
