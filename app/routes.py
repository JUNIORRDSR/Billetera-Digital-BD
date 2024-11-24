from flask import render_template, request, redirect
from app import app
from app.bussines.Consignacion import Consignacion
from app.bussines.Usuario import Usuario

# Rutas de páginas principales
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', title='Inicio')


# ruta para la página de inicio
@app.route('/app/templates/pages/inicio.html')
def inicio():
    return render_template('pages/inicio.html', title='Inicio')

# ruta para la página de login
@app.route('/app/templates/pages/login.html')
def login():
    return render_template('pages/login.html', title='Iniciar sesión')
@app.route('/app/templates/pages/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        tipo_de_id = request.form['id-type']
        numero_documento = request.form['id-number']
        contraseña = request.form['password']
        usuario = Usuario()
        usuario_logueado = usuario.iniciar_sesion(tipo_de_id, numero_documento, contraseña)
        if usuario_logueado:
            return redirect('pages/inicio.html')  # Redirigir a la página de inicio
        else:
            return redirect('pages/login.html?error=1')  # Redirigir con error

    return render_template('pages/login.html')




# ruta para la página de registro
@app.route('/app/templates/pages/register.html')
def register():
    return render_template('pages/register.html', title='Registro')
@app.route('/app/templates/pages/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        tipo_de_id = request.form['id-type']
        nombre = request.form['full-name']
        apellido = request.form['last-name']  # Asegúrate de que este campo esté en el formulario
        numero_documento = request.form['id-number']
        telefono = request.form['phone']
        correo = request.form['email']
        fecha_nacimiento = request.form['birthdate']
        contraseña = request.form['password']  # Asegúrate de que este campo esté en el formulario
        usuario = Usuario()
        if usuario.registrar_usuario(tipo_de_id, nombre, apellido, numero_documento, telefono, correo, fecha_nacimiento):
            return redirect('pages/inicio.html')  # Redirigir a la página de inicio
        else:
            return redirect('pages/register.html?error=1')  # Redirigir con error

    return render_template('pages/register.html')




# ruta para la página de retiros
@app.route('/app/templates/pages/retiros.html')
def retiros():
    return render_template('pages/retiros.html', title='Retiros')

# ruta para la página de transferencias
@app.route('/app/templates/pages/transferencias.html')
def transferencias():
    return render_template('pages/transferencias.html', title='Transferencias')

@app.route('/app/templates/pages/transferencias.html', methods=['POST'])
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
    return render_template('pages/pagos.html', title='Pagos')

# Rutas de páginas de Movimientos
@app.route('/app/templates/pages/movimientos.html')
def movimientos():
    return render_template('pages/movimientos.html', title='Movimientos')

# Rutas de páginas de Consignaciones
@app.route('/app/templates/pages/consignaciones.html')
def consignaciones():
    return render_template('pages/consignaciones.html', title='Consignaciones')

# Rutas de páginas de Configuración
@app.route('/app/templates/pages/configuracion.html')
def configuracion():
    return render_template('pages/configuracion.html', title='Configuración')
