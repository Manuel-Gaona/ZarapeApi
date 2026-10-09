from marshmallow import Schema, fields, validate

from app.schemas.base import Texto, campo_foto, largo


def hora():
    return fields.String(
        required=True,
        validate=validate.Regexp(
            r"^([01]\d|2[0-3]):[0-5]\d$", error="Usa el formato de 24 horas HH:MM."
        ),
    )


class SucursalSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = Texto(required=True, validate=largo(120))
    calle = Texto(required=True, validate=largo(120))
    numero = Texto(required=True, validate=largo(20))
    colonia = Texto(required=True, validate=largo(120))
    ciudad = Texto(required=True, validate=largo(80))
    estado = Texto(required=True, validate=largo(80))
    codigo_postal = Texto(load_default="", validate=largo(10, minimo=0))
    latitud = Texto(load_default="", validate=largo(30, minimo=0))
    longitud = Texto(load_default="", validate=largo(30, minimo=0))
    foto = campo_foto()
    url = Texto(load_default="", validate=largo(255, minimo=0))
    hora_apertura = hora()
    hora_cierre = hora()
