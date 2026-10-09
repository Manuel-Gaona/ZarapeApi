from marshmallow import Schema, fields, validate

from app.models.empleado import PUESTOS
from app.schemas.base import Texto, largo


class EmpleadoSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = Texto(required=True, validate=largo(80))
    apellido_paterno = Texto(required=True, validate=largo(80))
    apellido_materno = Texto(load_default="", validate=largo(80, minimo=0))
    puesto = fields.String(
        required=True,
        validate=validate.OneOf(PUESTOS, error="El puesto no es válido."),
    )
