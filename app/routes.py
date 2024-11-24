from flask import render_template
from app import app

# Rutas de páginas principales
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', title='Inicio')

@app.route('/app/templates/pages/inicio.html')
def inicio():
    return render_template('pages/inicio.html', title='Inicio')

@app.route('/app/templates/pages/login.html')
def login():
    return render_template('pages/login.html', title='Iniciar sesión')

@app.route('/app/templates/pages/register.html')
def register():
    return render_template('pages/register.html', title='Registro')

@app.route('/app/templates/pages/retiros.html')
def retiros():
    return render_template('pages/retiros.html', title='Retiros')

@app.route('/app/templates/pages/transferencias.html')
def transferencias():
    return render_template('pages/transferencias.html', title='Transferencias')

@app.route('/app/templates/pages/pagos.html')
def pagos():
    return render_template('pages/pagos.html', title='Pagos')

@app.route('/app/templates/pages/movimientos.html')
def movimientos():
    return render_template('pages/movimientos.html', title='Movimientos')

@app.route('/app/templates/pages/consignaciones.html')
def consignaciones():
    return render_template('pages/consignaciones.html', title='Consignaciones')

@app.route('/app/templates/pages/configuracion.html')
def configuracion():
    return render_template('pages/configuracion.html', title='Configuración')
