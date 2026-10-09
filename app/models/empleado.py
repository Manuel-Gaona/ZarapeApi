from app.extensions import db
from app.models.base import FechasMixin

PUESTOS = ["Administrador", "Cocinero", "Cajero", "Mesero"]


class Empleado(FechasMixin, db.Model):
    __tablename__ = "empleados"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido_paterno = db.Column(db.String(80), nullable=False)
    apellido_materno = db.Column(db.String(80), nullable=False, default="")
    puesto = db.Column(db.String(40), nullable=False)
