# coding: utf-8
from crud_tareas import db, ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema 

class TareaDetalle(db.Model):
    __tablename__ = 'tarea_detalle'

    tarea_detalle_id = db.Column(db.Integer, primary_key=True)
    tarea_id = db.Column(db.ForeignKey('tarea.tarea_id'), index=True)
    tarea_nombre = db.Column(db.String(50))
    tarea_descripcion = db.Column(db.String(50))
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.String(20))
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.String(20))
    ultimo_detalle = db.Column(db.Integer)
    register_state = db.Column(db.Integer)

    tarea = db.relationship('Tarea', primaryjoin='TareaDetalle.tarea_id == Tarea.tarea_id', backref='tarea_detalles')

    def __init__(self, tarea_detalle_id = None, tarea_id = None, tarea_nombre = None, tarea_descripcion = None, created_at = None, created_by = None, updated_at = None, updated_by = None, ultimo_detalle = None, register_state = None):
        self.tarea_detalle_id = tarea_detalle_id
        self.tarea_id = tarea_id
        self.tarea_nombre = tarea_nombre
        self.tarea_descripcion = tarea_descripcion
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.ultimo_detalle = ultimo_detalle
        self.register_state = register_state

class TareaDetalleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TareaDetalle
        load_instance = True