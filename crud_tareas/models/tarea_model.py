from crud_tareas import db, ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Tarea(db.Model):
    __tablename__ = 'tarea'

    tarea_id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.String(50))
    register_state = db.Column(db.Integer, server_default=db.FetchedValue())

    def __init__(self,  tarea_id = None,  created_at = None, created_by = None, updated_at = None, updated_by = None, register_state = None):
        self.tarea_id = tarea_id
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.register_state = register_state

class TareaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tarea
        load_instance = True