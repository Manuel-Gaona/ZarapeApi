"""Guardado y borrado de las imágenes subidas.

En la base de datos solo se guarda la ruta pública, por ejemplo
"/uploads/3f2a9c.jpg". El archivo vive en la carpeta UPLOAD_FOLDER.
"""

import os
import shutil
import uuid

from flask import current_app

from app.utils.errores import ErrorApi

PREFIJO = "/uploads/"


def _extension(nombre_archivo):
    return nombre_archivo.rsplit(".", 1)[-1].lower() if "." in nombre_archivo else ""


def _ruta_nueva(extension):
    """Genera un nombre único: así nunca se usa el nombre que mandó el cliente."""
    nombre = f"{uuid.uuid4().hex}.{extension}"
    return nombre, os.path.join(current_app.config["UPLOAD_FOLDER"], nombre)


def guardar_imagen(archivo):
    """Guarda un archivo recibido en un formulario y devuelve su ruta pública."""
    extension = _extension(archivo.filename or "")
    if extension not in current_app.config["EXTENSIONES_IMAGEN"]:
        raise ErrorApi("Solo se permiten imágenes PNG, JPG o WEBP.", 400)

    nombre, destino = _ruta_nueva(extension)
    archivo.save(destino)
    return PREFIJO + nombre


def copiar_imagen(origen):
    """Copia una imagen que ya está en el disco (la usan los datos de ejemplo)."""
    nombre, destino = _ruta_nueva(_extension(origen))
    shutil.copyfile(origen, destino)
    return PREFIJO + nombre


def borrar_imagen(foto):
    """Borra el archivo de una foto que ya no usa ningún registro."""
    if not foto or not foto.startswith(PREFIJO):
        return
    # basename evita que una ruta manipulada salga de la carpeta de imágenes
    nombre = os.path.basename(foto)
    ruta = os.path.join(current_app.config["UPLOAD_FOLDER"], nombre)
    if os.path.isfile(ruta):
        os.remove(ruta)


def reemplazar_imagen(foto_anterior, foto_nueva):
    """Si el registro cambió de foto, borra la anterior."""
    if foto_anterior != foto_nueva:
        borrar_imagen(foto_anterior)
