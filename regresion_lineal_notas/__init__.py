import os
from flask import Flask
from flask_restful import Api

from config import app_config

app = Flask(__name__)
api = Api(app)

#ma = SQLAlchemyAutoSchema()

config_name = os.getenv('FLASK_ENV')
app.config.from_object(app_config[config_name])
#db = SQLAlchemy(app)

#from regre .routes import crud_tareas_routes
#from crud_tareas.controllers import tarea_automatica_prueba

from regresion_lineal_notas.routes import regresion_lineal_notas_route
from regresion_lineal_notas.controllers import regresion_lineal_notas


