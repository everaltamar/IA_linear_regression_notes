from regresion_lineal_notas import api
from regresion_lineal_notas.controllers import regresion_lineal_notas

api.add_resource(regresion_lineal_notas.EntrenarModelo ,"/api/reg_lineal/entrenarModelo")
api.add_resource(regresion_lineal_notas.PredecirModelo ,"/api/reg_lineal/predecirModelo")





