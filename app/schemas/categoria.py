from marshmallow import Schema, fields


class CategoriaSchema(Schema):
    id = fields.Integer()
    nombre = fields.String()
    tipo = fields.String()
