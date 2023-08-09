from flask import Flask
from flask import (
    render_template,
    request
)
from flask_login import LoginManager
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

from config import config

# Models
from models.model_user import ModelUser

# Entities
from models.entities.user import User

app = Flask(__name__)
csrf = CSRFProtect()
mysql = MySQL(app)
login_manager_app = LoginManager(app)


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
    return render_template('auth/login.html')


if __name__ == '__main__':
    # Se selecciona el ambiente
    config_name = 'development'
    csrf.init_app(app)
    app.config.from_object(config[config_name])
    app.run(port=app.config['PORT'], host=app.config['HOST'])
