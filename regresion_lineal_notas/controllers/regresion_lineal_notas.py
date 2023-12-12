from pandas import core
from sklearn.linear_model import LinearRegression
import numpy as np
from flask_restful import Resource,reqparse

class EntrenarModelo(Resource):
    modelo_lineal_entrenado = None

    def post(self):   
        try:
                #prueba, y = mx + b

                horas_estudio = np.array([2, 4, 6, 8, 10, 12, 14]).reshape(-1,1)
                calificaciones = np.array([20, 40, 60, 80, 90, 95, 100])

                modelo_lineal = LinearRegression()
                modelo_lineal = modelo_lineal.fit(horas_estudio,calificaciones)

                EntrenarModelo.modelo_lineal_entrenado = modelo_lineal

                r_square = modelo_lineal.score(horas_estudio, calificaciones)

                return r_square
        
        except Exception as e:
            return str("Error interno")

class PredecirModelo(Resource):
    def post(self):
        try:
                parser = reqparse.RequestParser()
                parser.add_argument('horas_estudio', type=int, location="json")

                args = parser.parse_args()
                horas_estudio = args['horas_estudio']

                horas_estudio_prueba = np.array([[horas_estudio]]).reshape(-1,1)

                modelo_lineal = EntrenarModelo.modelo_lineal_entrenado 

                calificaciones = modelo_lineal.predict(horas_estudio_prueba)[0]
                calificaciones = round(calificaciones,2)

                return f"Su calificacion sera: {calificaciones}"
           
        except Exception as e:
            return str(e)














