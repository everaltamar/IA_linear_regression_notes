from crud_tareas import api
from crud_tareas.controllers import crud_tareas_controller

api.add_resource(crud_tareas_controller.ListadoTareas ,"/api/crud_tareas/listadoTareas")
api.add_resource(crud_tareas_controller.CrearTarea ,"/api/crud_tareas/CrearTarea")
api.add_resource(crud_tareas_controller.EliminarTarea ,"/api/crud_tareas/EliminarTarea")
api.add_resource(crud_tareas_controller.ActualizarTarea ,"/api/crud_tareas/ActualizarTarea")



