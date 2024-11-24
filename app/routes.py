from flask import render_template
from app import app

# Rutas de páginas principales
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', title='Inicio')