from datetime import datetime
import json
from crud_tareas import db, app
from flask_restful import Resource,reqparse
from sqlalchemy import text
from flask import jsonify
from crud_tareas.models import tarea_model, tarea_detalle_model

#git
class ListadoTareas(Resource):
    def get(self):
        try:
            tareas = tarea_model.Tarea.query.filter(tarea_model.Tarea.register_state == 1).all()
            tarea_schema = tarea_model.TareaSchema(many=True)
            result = tarea_schema.dump(tareas) 
            return result
        except Exception as e:
            return str("Error interno")

class CrearTarea(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('tarea_nombre', type=str, location="json")
            parser.add_argument('tarea_descripcion', type=str, location="json")
            parser.add_argument('create_by', type=str, location="json")

            args = parser.parse_args()
            fecha = datetime.now()

            obj_tarea_nombre= args['tarea_nombre']
            obj_tarea_descripcion = args['tarea_descripcion']
            obj_created_by = args['create_by']
            obj_register_state = 1
            obj_ultimo_detalle = 1

            tarea = tarea_model.Tarea(
            #tarea_id = obj_tarea_id,
            created_at = fecha, 
            created_by = obj_created_by, 
            updated_at = None, 
            updated_by = None, 
            register_state = obj_register_state 
            ) 
            db.session.add(tarea)
            db.session.flush()

            tarea_detalle = tarea_detalle_model.TareaDetalle(
            #tarea_detalle_id = obj_tarea_detalle_id,
            tarea_id = tarea.tarea_id,
            tarea_nombre = obj_tarea_nombre,
            tarea_descripcion = obj_tarea_descripcion,
            created_at = tarea.created_at,
            created_by = tarea.created_by,
            updated_at = None,
            updated_by = None,
            ultimo_detalle = obj_ultimo_detalle,
            register_state = obj_register_state,
            )
            db.session.add(tarea_detalle)

            db.session.commit()
                
            return "Tarea Creada"
        except Exception as e:
            return str("Error interno")

class EliminarTarea(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('tarea_id', type=int)
            parser.add_argument('updated_by', type=str)

            fecha = datetime.now()

            args = parser.parse_args()
            obj_tarea_id = args['tarea_id']
            obj_updated_by = args['updated_by']

            obj_tarea = tarea_model.Tarea
            obj_tarea_detalle = tarea_detalle_model.TareaDetalle

            tarea_eliminar = db.session.query(obj_tarea).filter_by(tarea_id=obj_tarea_id, register_state=1).first()

            if not tarea_eliminar:
                return "No existe este registro"

            db.session.query(obj_tarea)\
                .filter_by(tarea_id=obj_tarea_id, register_state=1)\
                .update({
                    obj_tarea.updated_at:fecha,
                    obj_tarea.updated_by:obj_updated_by,
                    obj_tarea.register_state: 0
                }, synchronize_session=False)
            
            db.session.query(obj_tarea_detalle)\
                .filter_by(tarea_id=obj_tarea_id, register_state=1)\
                .update({
                    obj_tarea_detalle.updated_at:fecha,
                    obj_tarea_detalle.updated_by:obj_updated_by,
                    obj_tarea_detalle.ultimo_detalle: 0,
                    obj_tarea_detalle.register_state:0
                }, synchronize_session=False)
            
            db.session.commit()            
            
            return "Tarea eliminada exitosamente"


        except Exception as e:
            return str("Error interno")

class ActualizarTarea(Resource):
    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('tarea_id', type=int)
            parser.add_argument('tarea_nombre', type=str)
            parser.add_argument('tarea_descripcion', type=str)
            parser.add_argument('updated_by', type=str)

            args = parser.parse_args()
            fecha = datetime.now()

            obj_tarea_id = args['tarea_id']
            obj_tarea_nombre = args['tarea_nombre']
            obj_tarea_descripcion = args['tarea_descripcion']
            obj_updated_by = args['updated_by']

            obj_tarea = tarea_model.Tarea
            obj_tarea_detalle = tarea_detalle_model.TareaDetalle

            db.session.query(obj_tarea)\
                .filter_by(tarea_id=obj_tarea_id, register_state=1)\
                .update({
                    obj_tarea.updated_at:fecha,
                    obj_tarea.updated_by:obj_updated_by
                }, synchronize_session=False)
            
            db.session.query(obj_tarea_detalle)\
                .filter_by(tarea_id=obj_tarea_id, register_state=1)\
                .update({
                    obj_tarea_detalle.updated_at:fecha,
                    obj_tarea_detalle.updated_by:obj_updated_by,
                    obj_tarea_detalle.ultimo_detalle: 0,
                    obj_tarea_detalle.register_state:0
                }, synchronize_session=False)
            
            #buscar el id de la tarea y guardarlo 
            tarea_datos = db.session.query(obj_tarea_detalle).first()
            
            # Crear un nuevo registro con los datos actualizados
            nueva_tarea_detalle = obj_tarea_detalle(
            tarea_id = tarea_datos.tarea_id,
            tarea_nombre = obj_tarea_nombre,
            tarea_descripcion = obj_tarea_descripcion,
            created_at = tarea_datos.created_at,
            created_by = tarea_datos.created_by,
            updated_at = fecha,
            updated_by = obj_updated_by,
            ultimo_detalle = 1,
            register_state = 1
            )

            db.session.add(nueva_tarea_detalle)
            db.session.commit()

            return "Tarea actualizada exitosamente"
            
        except Exception as e:
            return str(e)

def convertJson(result):
    rv = result.fetchall()
    row_headers = result.keys()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return json_data









