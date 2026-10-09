from marshmallow import Schema, fields, validate

from app.schemas.base import Texto, largo


class UsuarioSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = Texto(required=True, validate=largo(120, minimo=3))
    # load_only: la contraseña se recibe, pero nunca se devuelve en una respuesta
    password = fields.String(
        required=True,
        load_only=True,
        validate=validate.Length(min=6, error="Debe tener al menos {min} caracteres."),
    )


class LoginSchema(Schema):
    nombre = Texto(required=True)
    password = fields.String(required=True)
