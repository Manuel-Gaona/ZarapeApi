from app.extensions import db
from app.models.base import FechasMixin


class Sucursal(FechasMixin, db.Model):
    __tablename__ = "sucursales"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)

    # Dirección
    calle = db.Column(db.String(120), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    colonia = db.Column(db.String(120), nullable=False)
    ciudad = db.Column(db.String(80), nullable=False)
    estado = db.Column(db.String(80), nullable=False)
    codigo_postal = db.Column(db.String(10), nullable=False, default="")

    # Se guardan como texto porque el diseño las muestra en grados (66° 33' 9'' N)
    latitud = db.Column(db.String(30), nullable=False, default="")
    longitud = db.Column(db.String(30), nullable=False, default="")

    foto = db.Column(db.String(255))
    url = db.Column(db.String(255), nullable=False, default="")

    # Horario en formato de 24 horas "HH:MM"
    hora_apertura = db.Column(db.String(5), nullable=False)
    hora_cierre = db.Column(db.String(5), nullable=False)
