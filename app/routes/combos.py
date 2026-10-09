from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.extensions import db
from app.models import Combo, ComboDetalle, Producto
from app.schemas import ComboSchema
from app.utils.consultas import asignar, datos_json, filtrar_por_texto, obtener_o_404
from app.utils.errores import ErrorApi
from app.utils.imagenes import borrar_imagen, reemplazar_imagen

bp = Blueprint("combos", __name__, url_prefix="/api/combos")

schema = ComboSchema()


def construir_detalles(detalles):
    """Convierte [{producto_id, cantidad}] en objetos ComboDetalle."""
    ids = {detalle["producto_id"] for detalle in detalles}
    existentes = set(
        db.session.scalars(db.select(Producto.id).where(Producto.id.in_(ids)))
    )
    if ids != existentes:
        raise ErrorApi(
            "Revisa los datos del formulario.",
            400,
            {"detalles": ["Uno de los productos del combo ya no existe."]},
        )
    return [ComboDetalle(**detalle) for detalle in detalles]


@bp.get("")
def listar():
    consulta = db.select(Combo).order_by(Combo.nombre)
    consulta = filtrar_por_texto(
        consulta, request.args.get("buscar"), Combo.nombre, Combo.descripcion
    )
    return schema.dump(db.session.scalars(consulta), many=True)


@bp.get("/<int:id>")
def obtener(id):
    return schema.dump(obtener_o_404(Combo, id, "El combo"))


@bp.post("")
@jwt_required()
def crear():
    datos = schema.load(datos_json())
    detalles = construir_detalles(datos.pop("detalles"))

    combo = Combo(**datos, detalles=detalles)
    db.session.add(combo)
    db.session.commit()
    return schema.dump(combo), 201


@bp.put("/<int:id>")
@jwt_required()
def actualizar(id):
    combo = obtener_o_404(Combo, id, "El combo")
    foto_anterior = combo.foto

    datos = schema.load(datos_json())
    # Reemplaza la lista completa: los detalles anteriores se borran solos
    combo.detalles = construir_detalles(datos.pop("detalles"))
    asignar(combo, datos)
    db.session.commit()

    reemplazar_imagen(foto_anterior, combo.foto)
    return schema.dump(combo)


@bp.delete("/<int:id>")
@jwt_required()
def eliminar(id):
    combo = obtener_o_404(Combo, id, "El combo")
    foto = combo.foto

    db.session.delete(combo)
    db.session.commit()

    borrar_imagen(foto)
    return "", 204
