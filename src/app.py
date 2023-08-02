from flask import Flask

from config import config

app = Flask(__name__)


@app.route('/')
def index():
    return 'ok'


if __name__ == '__main__':
    # Se selecciona el ambiente
    config_name = 'development'
    app.config.from_object(config[config_name])
    app.run(port=app.config['PORT'], host=app.config['HOST'])
