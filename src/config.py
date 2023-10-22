import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')


class Config:
    DEBUG = False
    TESTING = False
    PORT = 5000
    HOST = '127.0.0.1'
    SECRET_KEY = 'Clave_Secreta'


class ProductionConfig(Config):
    HOST = '0.0.0.0'
    SECRET_KEY = os.getenv('SECRET_KEY')
    MYSQL_HOST = os.getenv('DATABASE_HOST_UR')
    MYSQL_USER = os.getenv('DATABASE_USERNAME')
    MYSQL_PASSWORD = os.getenv('DATABASE_PASSWORD')
    MYSQL_DB = os.getenv('DATABASE_NAME')


class DevelopmentConfig(Config):
    DEBUG = True
    HOST = 'localhost'
    SECRET_KEY = 'Clave_Secreta'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'pt_data_dev'


class TestingConfig(Config):
    TESTING = True
    HOST = '0.0.0.0'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'pt_data_dev'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
