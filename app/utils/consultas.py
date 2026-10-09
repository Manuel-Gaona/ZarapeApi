"""Funciones pequeñas que se repiten en todas las rutas."""

from flask import request
from sqlalchemy import or_

from app.extensions import db
from app.utils.errores import ErrorApi


def datos_json():
    """Cuerpo JSON de la petición (o un diccionario vacío si no viene)."""
    return request.get_json(silent=True) or {}


def obtener_o_404(modelo, id, nombre="El registro"):
    registro = db.session.get(modelo, id)
    if registro is None:
        raise ErrorApi(f"{nombre} no existe.", 404)
    return registro


def filtrar_por_texto(consulta, texto, *columnas):
    """Deja solo las filas donde alguna columna contiene el texto buscado."""
    texto = (texto or "").strip()
    if not texto:
        return consulta
    patron = f"%{texto}%"
    return consulta.where(or_(*[columna.ilike(patron) for columna in columnas]))


def asignar(registro, datos):
    """Copia cada valor del diccionario al atributo del mismo nombre."""
    for campo, valor in datos.items():
        setattr(registro, campo, valor)
