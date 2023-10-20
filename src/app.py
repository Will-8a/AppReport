from flask import Flask
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash
)
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    current_user
)
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

from config import config
from rest_api import rest_api

# Models
from models.model_user import ModelUser

# Entities
from models.entities.user import User

app = Flask(__name__)
csrf = CSRFProtect()
mysql = MySQL(app)
login_manager_app = LoginManager(app)
api = rest_api.RestApi()


@login_manager_app.user_loader
def load_user(cedula):
    return ModelUser.get_by_cedula(mysql, cedula)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Crea un objeto para almacenar los datos
        # del usuario
        entidad_usuario = User(
            cedula=request.form.get('username'),
            contrasena=request.form.get('password')
        )
        usuario_logeado = ModelUser.login(
            mysql=mysql,
            user=entidad_usuario
        )

        if usuario_logeado is None:
            flash('Usuario no encontrado')
            return render_template('auth/login.html')
        else:
            contrasena_valida = usuario_logeado.contrasena
            if contrasena_valida:
                login_user(usuario_logeado)
                return redirect(url_for('index'))
            else:
                flash('Contraseña invalida')
                return render_template('auth/login.html')
    return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash('Ha finalizado la sesion')
    return redirect(url_for('login'))


@app.route('/agregar_estudiante', methods=['POST'])
def create_usuario_estudiante():
    # Se convierte en un diccionario
    # los datos que se envian a la API
    request_cliente = request.json

    # Se guarda en la variable response
    # la respuesta del servidor
    respuesta_api = api.create_usuario_estudiante(
        mysql=mysql,
        current_user=current_user,
        request_cliente=request_cliente
    )
    return respuesta_api


@app.route('/agregar_tutor', methods=['POST'])
def create_usuario_tutor():
    # Se convierte en un diccionario
    # los datos que se envian a la API
    request_cliente = request.json

    # Se guarda en la variable response
    # la respuesta del servidor
    respuesta_api = api.create_usuario_tutor(
        mysql=mysql,
        current_user=current_user,
        request_cliente=request_cliente
    )
    return respuesta_api


@app.route('/nuevo_reporte', methods=['POST'])
def create_reporte():
    request_cliente = request.json

    respuesta_api = api.create_reporte(
        mysql=mysql,
        current_user=current_user,
        request_cliente=request_cliente
    )
    return respuesta_api


@app.route('/leer_estudiante', methods=['GET'])
def read_usuario_estudiante():
    cedula_estudiante = request.args.get('cedula_estudiante')
    request_cliente = {
        'cedula_estudiante': cedula_estudiante
    }
    respuesta_api = api.read_usuario_estudiante(
        mysql=mysql,
        current_user=current_user,
        request_cliente=request_cliente
    )
    return respuesta_api


@app.route('/leer_tutor', methods=['GET'])
def read_usuario_tutor():
    cedula_tutor = request.args.get('cedula_tutor')
    request_cliente = {
        'cedula_tutor': cedula_tutor
    }
    respuesta_api = api.read_usuario_tutor(
        mysql=mysql,
        current_user=current_user,
        request_cliente=request_cliente
    )
    return respuesta_api


@app.route('/leer_reporte', methods=['GET'])
def read_reporte_especifico():
    cedula_estudiante = request.args.get('cedula_estudiante')
    numero_reporte = request.args.get('numero_reporte')

    request_cliente = {
        'cedula_estudiante': cedula_estudiante,
        'numero_reporte': numero_reporte
    }
    respuesta_api = api.read_reporte_especifico(
        mysql=mysql,
        current_user=current_user,
        request_cliente=request_cliente
    )
    return respuesta_api


@app.route('/leer_reportes_estudiante', methods=['GET'])
def read_reportes_estudiante_especifico():
    cedula_estudiante = request.args.get('cedula_estudiante')

    request_cliente = {
        'cedula_estudiante': cedula_estudiante
    }
    respuesta_api = api.read_reportes_estudiante_especifico(
        mysql=mysql,
        current_user=current_user,
        request_cliente=request_cliente
    )
    return respuesta_api


@app.route('/leer_reportes_tutorados', methods=['GET'])
def read_reportes_tutorados():
    cedula_tutor = request.args.get('cedula_tutor')

    request_cliente = {
        'cedula_tutor': cedula_tutor
    }

    respuesta_api = api.read_reportes_tutorados(
        mysql=mysql,
        current_user=current_user,
        request_cliente=request_cliente
    )

    return respuesta_api


@app.route('/actualizar_estudiante', methods=['PUT'])
def update_usuario_estudiante():
    request_cliente = request.json
    respuesta_api = api.update_usuario_estudiante(
        mysql=mysql,
        current_user=current_user,
        request_cliente=request_cliente
    )
    return respuesta_api


@app.route('/actualizar_tutor', methods=['PUT'])
def update_usuario_tutor():
    request_cliente = request.json
    respuesta_api = api.update_usuario_tutor(
        mysql=mysql,
        current_user=current_user,
        request_cliente=request_cliente
    )
    return respuesta_api


@app.route('/actualizar_estatus_reporte', methods=['PUT'])
def update_estatus_reporte():
    request_cliente = request.json
    respuesta_api = api.update_estatus_reporte(
        mysql=mysql,
        current_user=current_user,
        request_cliente=request_cliente
    )

    return respuesta_api


@app.route('/actualizar_reporte',  methods=['PUT'])
def update_reporte_especifico():
    request_cliente = request.json

    respuesta_api = api.update_reporte_especifico(
        mysql=mysql,
        current_user=current_user,
        request_cliente=request_cliente
    )
    return respuesta_api


@app.route('/eliminar_estudiante', methods=['DELETE'])
def delete_usuario_estudiante():
    request_cliente = request.json
    respuesta_api = api.delete_usuario_estudiante(
        mysql=mysql,
        current_user=current_user,
        request_cliente=request_cliente
    )
    return respuesta_api


@app.route('/eliminar_tutor', methods=['DELETE'])
def delete_usuario_tutor():
    request_cliente = request.json
    respuesta_api = api.delete_usuario_tutor(
        mysql=mysql,
        current_user=current_user,
        request_cliente=request_cliente
    )
    return respuesta_api


if __name__ == '__main__':
    # Se selecciona el ambiente
    config_name = 'development'
    csrf.init_app(app)
    app.config.from_object(config[config_name])
    app.run(port=app.config['PORT'], host=app.config['HOST'])
