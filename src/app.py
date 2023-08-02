from flask import Flask
from flask import render_template

from config import config

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Se selecciona el ambiente
    config_name = 'development'
    app.config.from_object(config[config_name])
    app.run(port=app.config['PORT'], host=app.config['HOST'])
