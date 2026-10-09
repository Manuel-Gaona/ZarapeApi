"""Piezas compartidas por todos los esquemas.

Un esquema de marshmallow hace dos trabajos:
  - load: valida los datos que envía el cliente (JSON -> diccionario limpio).
  - dump: convierte un modelo en un diccionario listo para responder como JSON.
"""

from marshmallow import fields, validate

# Mensajes de validación en español
fields.Field.default_error_messages.update(
    {
        "required": "Este campo es obligatorio.",
        "null": "Este campo no puede estar vacío.",
    }
)


class Texto(fields.String):
    """Texto al que se le quitan los espacios sobrantes de los extremos."""

    def _deserialize(self, value, attr, data, **kwargs):
        return super()._deserialize(value, attr, data, **kwargs).strip()


def largo(maximo, minimo=1):
    if minimo == 0:
        return validate.Length(max=maximo, error="Debe tener máximo {max} caracteres.")
    return validate.Length(
        min=minimo, max=maximo, error="Debe tener entre {min} y {max} caracteres."
    )


def campo_precio():
    return fields.Float(
        required=True,
        validate=validate.Range(min=0, error="El precio no puede ser negativo."),
    )


def campo_foto():
    """Ruta de una imagen subida antes con POST /api/imagenes."""
    return fields.String(
        allow_none=True,
        load_default=None,
        validate=validate.Regexp(r"^/uploads/[\w.-]+$", error="La foto no es válida."),
    )
