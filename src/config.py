class Config:
    DEBUG = False
    TESTING = False
    PORT = 5000
    HOST = '127.0.0.1'
    SECRET_KEY = 'Clave_Secreta'


class ProductionConfig(Config):
    HOST = '0.0.0.0'


class DevelopmentConfig(Config):
    DEBUG = True
    HOST = 'localhost'
    SECRET_KEY = 'Clave_Secreta'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'pt_data'


class TestingConfig(Config):
    TESTING = True
    HOST = '127.0.0.1'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
