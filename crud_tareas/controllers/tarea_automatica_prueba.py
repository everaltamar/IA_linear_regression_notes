from datetime import datetime
import json, click, os
from crud_tareas import db, app
from flask_restful import Resource,reqparse
from sqlalchemy import text
from flask import jsonify
from crud_tareas.models import tarea_model, tarea_detalle_model


@app.cli.command('tareaprueba')
@click.pass_context
def prue(ctx):
    try:
        result = "holaaa"
        print(result)
        click.echo("tarea realizada")
    except Exception as e:
        click.echo("error tarea")
        return str("Error interno")
