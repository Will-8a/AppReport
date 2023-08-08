from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

from config import config

app = Flask(__name__)
csrf = CSRFProtect()
mysql = MySQL(app)


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
