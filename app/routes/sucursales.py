from flask import Blueprint, request
from flask_jwt_extended import verify_jwt_in_request

from app.extensions import db
from app.models import Sucursal
from app.schemas import SucursalSchema
from app.utils.consultas import asignar, datos_json, filtrar_por_texto, obtener_o_404
from app.utils.imagenes import borrar_imagen, reemplazar_imagen

bp = Blueprint("sucursales", __name__, url_prefix="/api/sucursales")

schema = SucursalSchema()


@bp.before_request
def exigir_sesion():
    verify_jwt_in_request()


@bp.get("")
def listar():
    consulta = db.select(Sucursal).order_by(Sucursal.nombre)
    consulta = filtrar_por_texto(
        consulta,
        request.args.get("buscar"),
        Sucursal.nombre,
        Sucursal.calle,
        Sucursal.colonia,
        Sucursal.ciudad,
        Sucursal.estado,
    )
    return schema.dump(db.session.scalars(consulta), many=True)


@bp.post("")
def crear():
    sucursal = Sucursal(**schema.load(datos_json()))
    db.session.add(sucursal)
    db.session.commit()
    return schema.dump(sucursal), 201


@bp.put("/<int:id>")
def actualizar(id):
    sucursal = obtener_o_404(Sucursal, id, "La sucursal")
    foto_anterior = sucursal.foto

    asignar(sucursal, schema.load(datos_json()))
    db.session.commit()

    reemplazar_imagen(foto_anterior, sucursal.foto)
    return schema.dump(sucursal)


@bp.delete("/<int:id>")
def eliminar(id):
    sucursal = obtener_o_404(Sucursal, id, "La sucursal")
    foto = sucursal.foto

    db.session.delete(sucursal)
    db.session.commit()

    borrar_imagen(foto)
    return "", 204
