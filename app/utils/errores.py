"""Manejo centralizado de errores.

Todas las respuestas de error tienen la misma forma, para que el frontend
las pueda tratar igual:

    { "mensaje": "Texto para mostrar", "errores": { "campo": ["detalle"] } }
"""

from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import HTTPException

from app.extensions import db, jwt

MENSAJES_HTTP = {
    404: "El recurso solicitado no existe.",
    405: "Método no permitido.",
    413: "El archivo es demasiado grande (máximo 5 MB).",
}


class ErrorApi(Exception):
    """Error de negocio que se responde al cliente con un código HTTP."""

    def __init__(self, mensaje, codigo=400, errores=None):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.codigo = codigo
        self.errores = errores or {}


def respuesta_error(mensaje, codigo, errores=None):
    return {"mensaje": mensaje, "errores": errores or {}}, codigo


def registrar_manejadores_de_errores(app):
    @app.errorhandler(ErrorApi)
    def error_api(error):
        return respuesta_error(error.mensaje, error.codigo, error.errores)

    @app.errorhandler(ValidationError)
    def error_validacion(error):
        return respuesta_error("Revisa los datos del formulario.", 400, error.messages)

    @app.errorhandler(IntegrityError)
    def error_integridad(_):
        db.session.rollback()
        return respuesta_error(
            "No se pudo completar: el registro está relacionado con otros datos.", 409
        )

    @app.errorhandler(HTTPException)
    def error_http(error):
        return respuesta_error(MENSAJES_HTTP.get(error.code, error.description), error.code)

    @app.errorhandler(Exception)
    def error_inesperado(error):
        db.session.rollback()
        app.logger.exception(error)
        return respuesta_error("Ocurrió un error inesperado en el servidor.", 500)

    # Errores del token de sesión: siempre se responden como 401
    @jwt.unauthorized_loader
    def falta_token(_):
        return respuesta_error("Debes iniciar sesión.", 401)

    @jwt.invalid_token_loader
    def token_invalido(_):
        return respuesta_error("La sesión no es válida. Inicia sesión de nuevo.", 401)

    @jwt.expired_token_loader
    def token_expirado(_encabezado, _datos):
        return respuesta_error("La sesión expiró. Inicia sesión de nuevo.", 401)
