from marshmallow import Schema, fields, validate

from app.models.categoria import TIPOS_PRODUCTO
from app.schemas.base import Texto, campo_foto, campo_precio, largo
from app.schemas.categoria import CategoriaSchema


class ProductoSchema(Schema):
    id = fields.Integer(dump_only=True)
    tipo = fields.String(
        required=True,
        validate=validate.OneOf(TIPOS_PRODUCTO, error="Debe ser alimento o bebida."),
    )
    nombre = Texto(required=True, validate=largo(120))
    descripcion = Texto(load_default="", validate=largo(500, minimo=0))
    foto = campo_foto()
    precio = campo_precio()

    # Se recibe solo el id de la categoría y se responde la categoría completa
    categoria_id = fields.Integer(required=True)
    categoria = fields.Nested(CategoriaSchema, dump_only=True)
