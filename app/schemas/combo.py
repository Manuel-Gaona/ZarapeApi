from marshmallow import Schema, fields, validate

from app.schemas.base import Texto, campo_foto, campo_precio, largo
from app.schemas.producto import ProductoSchema


class ComboDetalleSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto_id = fields.Integer(required=True)
    cantidad = fields.Integer(
        required=True,
        validate=validate.Range(min=1, error="La cantidad mínima es 1."),
    )
    producto = fields.Nested(
        ProductoSchema(only=("id", "nombre", "precio", "tipo")), dump_only=True
    )


class ComboSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = Texto(required=True, validate=largo(120))
    descripcion = Texto(load_default="", validate=largo(500, minimo=0))
    foto = campo_foto()
    precio = campo_precio()
    detalles = fields.List(
        fields.Nested(ComboDetalleSchema),
        required=True,
        validate=validate.Length(min=1, error="Agrega al menos un producto al combo."),
    )
