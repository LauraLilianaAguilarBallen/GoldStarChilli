from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/work.db'
db = SQLAlchemy(app)


class Registro(db.Model):  # Genera los datos de la tabla registros
    identificacion = db.Column(db.Integer, primary_key=True)
    tipodocumento = db.Column(db.String(10))
    nombres = db.Column(db.String(10))
    apellidos = db.Column(db.String(10))
    telefono = db.Column(db.String(10))
    correo = db.Column(db.String(20))
    fechanacimiento = db.Column(db.String(10))
    direccion = db.Column(db.String(10))


class Usuario(db.Model):  # Genera los datos de la tabla usuario
    usuario = db.Column(db.String(10), primary_key=True)
    identificacion = db.Column(db.Integer)
    contraseña = db.Column(db.Integer)


@app.route('/')  # Incia página principal
def home():
    return render_template('index.html')


@app.route('/login/registrarse/')  # Inicia página regsitrarse
def registro():
    return render_template('registrarse.html')


@app.route('/registro/', methods=['POST'])  # Insertar datos generales de usuario
def creater():
    regis = Registro(identificacion=request.form['d2'], tipodocumento=request.form['d1'], nombres=request.form['d3'],
                     apellidos=request.form['d4'], telefono=request.form['d5'], correo=request.form['d6'],
                     fechanacimiento=request.form['d7'],
                     direccion=request.form['d8'])  # 1) content de .py 2) content del html
    db.session.add(regis)  # comensar a guardar los datos
    db.session.commit()
    return redirect(url_for('user'))


@app.route('/user')  # Inciar página principal para registrar usuario
def user(named=None):
    return render_template('user.html', name=named)


@app.route('/userd', methods=['POST'])  # Insert datos de login para el usuario
def createu():
    userc = Usuario(usuario=request.form['u1'], identificacion=request.form['u2'],
                    contraseña=request.form['u3'])  # 1) content de .py 2) content del html
    db.session.add(userc)  # comensar a guardar los datos
    db.session.commit()
    return redirect(url_for('login'))


@app.route('/loginu/', methods=['POST'])  # Inicia sesión y validad los datos
def loginu():
    iden = request.form['l1']
    contra = request.form['l2']
    users = Usuario.query.filter_by(identificacion=iden).first()
    if users:
        userc = Usuario.query.filter_by(contraseña=contra).first()
        if userc:
            return render_template('mostrarMenu.html')  # agregar lapágina leugo logiarse
        else:
            return render_template('alert.html')
    else:
        return render_template('registrarse.html')


@app.route('/error/')  # Iniciar página de error en los datos
def error(name=None):
    return render_template('login.html', name=name)


@app.route('/login/')  # Inicia página login
def login(nameq=None):
    return render_template('login.html', name=nameq)


""" -------- ------------------ -------------------- ----------------------"""
"""                                --                                      """
""" -------- ------------------ -------------------- ----------------------"""


@app.route('/loginu/gestionusuario/')  #
def gestionUsuario(nameq=None):
    return render_template('gestionUsuario.html', name=nameq)


@app.route('/loginu/perfilusuario/')  #
def perfilusuario(nameq=None):
    return render_template('perfil.html', name=nameq)


@app.route('/loginu/perfilusuario/gestioncomentarios/')  #
def gestioncomentarios(nameq=None):
    return render_template('gestionComentarios.html', name=nameq)


@app.route('/menu/')  #
def menu(nameq=None):
    return render_template('mostrarMenu.html', name=nameq)


@app.route('/loginu/listadeseos/')  #
def listadeseos(nameq=None):
    return render_template('listarDeseos.html', name=nameq)


@app.route('/loginu/pedidos/')  #
def pedidos(nameq=None):
    return render_template('pedidos.html', name=nameq)


@app.route('/loginu/detallesplato/')  #
def detallesplato(nameq=None):
    return render_template('detallesPlato.html', name=nameq)
