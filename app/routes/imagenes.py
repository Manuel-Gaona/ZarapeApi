"""Subida y entrega de imágenes.

Flujo que sigue el frontend:
  1. Sube el archivo con POST /api/imagenes y recibe {"foto": "/uploads/abc.jpg"}.
  2. Envía esa ruta en el campo "foto" al guardar el alimento, combo o sucursal.
"""

from flask import Blueprint, current_app, request, send_from_directory
from flask_jwt_extended import jwt_required

from app.utils.errores import ErrorApi
from app.utils.imagenes import guardar_imagen

bp = Blueprint("imagenes", __name__, url_prefix="/api/imagenes")
bp_archivos = Blueprint("archivos", __name__)


@bp.post("")
@jwt_required()
def subir():
    archivo = request.files.get("archivo")
    if archivo is None or not archivo.filename:
        raise ErrorApi("Selecciona una imagen.", 400)

    return {"foto": guardar_imagen(archivo)}, 201


@bp_archivos.get("/uploads/<path:nombre>")
def ver(nombre):
    """Entrega una imagen guardada (send_from_directory impide salir de la carpeta)."""
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], nombre)
