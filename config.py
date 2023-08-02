import logging
from sqlalchemy.pool import NullPool

class Config:
    """ Common configurations """
    #SQLALCHEMY_ENGINE_OPTIONS = { "poolclass": NullPool }
    #CUSTOMER_SERVICE_NAME = "Name"
    #CUSTOMER_SERVICE_TEL_NUMBER = "5555555"


class DevelopmentConfig(Config):
    """ Development configurations """
    FLASK_DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123456@127.0.0.1/CRUD_TD'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_BINDS = {
        "otra_conexion": "mysql+pymysql://credenciales",
    }
    RUTA = "https://URL/api/"
    SENTRY_ENV = "development"
    logging.basicConfig(level=logging.INFO)


class QualityConfig(Config):
    """ QA Ambient configurations """
    FLASK_DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123456@127.0.0.1/CRUD_TD'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        "otra_conexion": "mysql+pymysql://credenciales",
    }
    RUTA = "https://URL/api/"
    SENTRY_ENV = "release"


class ProductionConfig(Config):
    """ Production configurations """
    FLASK_DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123456@127.0.0.1/CRUD_TD'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        "otra_conexion": "mysql+pymysql://credenciales",
    }
    RUTA = "https://URL/api/"
    SENTRY_ENV = "release"


app_config = {
    'dev': DevelopmentConfig,
    'qa':QualityConfig,
    'pro': ProductionConfig
}

#modelos 
#flask-sqlacodegen --flask --outfile tareas_model.py --tables tareas mysql+pymysql://root:admin123456@127.0.0.1/CRUD_TD

