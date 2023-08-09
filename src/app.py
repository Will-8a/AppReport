from flask import Flask
from flask import render_template
from flask_login import LoginManager
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

from config import config

# Models
from models.model_user import ModelUser

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
    return render_template('auth/login.html')


if __name__ == '__main__':
    # Se selecciona el ambiente
    config_name = 'development'
    csrf.init_app(app)
    app.config.from_object(config[config_name])
    app.run(port=app.config['PORT'], host=app.config['HOST'])
