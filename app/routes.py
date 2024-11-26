from flask import render_template, request, redirect
from app import app,db_connection as db
from app.bussines.Consignacion import Consignacion
from app.bussines.Usuario import Usuario

# Rutas de páginas principales
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


# ruta para la página de inicio
@app.route('/app/templates/pages/inicio.html')
def inicio():
    return render_template('pages/inicio.html')

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
@app.route('/app/templates/pages/transferencias.html')
def transferencias():
    return render_template('pages/transferencias.html')

@app.route('/app/templates/pages/transferencias.html')
def registrar_consignacion():
    data = request.form
    id_cuenta_origen = data['id_cuenta_origen']
    id_cuenta_destino = data['id_cuenta_destino']
    monto = data['monto']
    descripcion = data.get('descripcion', '')
    procedencia = data['procedencia']
    consignacion = Consignacion()
    if consignacion.registrar_consignacion(id_cuenta_origen, id_cuenta_destino, monto, descripcion, procedencia):
        return redirect('pages/transferencias.html')
    return redirect('pages/transferencias.html?error=1')

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
