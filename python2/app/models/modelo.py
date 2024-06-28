from flask import Flask
from app import db
import datetime

class Tareas(db.Model):
    id_tar = db.Column(db.Integer,Primary_Key=True )
    nombretar = db.Column(db.String(200), nullable=False)
    fecha_inicio = db.Column(db.Datetime,default=datetime.utcnow)
    fecha_fin = db.Column(db.Datetime)
    estado = db.Column(db.String(20,default='Por asignar'))
