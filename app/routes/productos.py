"""Productos del menú: alimentos y bebidas.

    GET /api/productos?tipo=alimento&buscar=torta
"""

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.extensions import db
from app.models import Categoria, ComboDetalle, Producto
from app.schemas import ProductoSchema
from app.utils.consultas import asignar, datos_json, filtrar_por_texto, obtener_o_404
from app.utils.errores import ErrorApi
from app.utils.imagenes import borrar_imagen, reemplazar_imagen

bp = Blueprint("productos", __name__, url_prefix="/api/productos")

schema = ProductoSchema()


def validar_categoria(datos):
    """La categoría debe existir y ser del mismo tipo que el producto."""
    categoria = db.session.get(Categoria, datos["categoria_id"])
    if categoria is None or categoria.tipo != datos["tipo"]:
        raise ErrorApi(
            "Revisa los datos del formulario.",
            400,
            {"categoria_id": ["Selecciona una categoría válida."]},
        )


@bp.get("")
def listar():
    consulta = db.select(Producto).order_by(Producto.nombre)

    tipo = request.args.get("tipo")
    if tipo:
        consulta = consulta.where(Producto.tipo == tipo)

    consulta = filtrar_por_texto(
        consulta, request.args.get("buscar"), Producto.nombre, Producto.descripcion
    )
    return schema.dump(db.session.scalars(consulta), many=True)


@bp.get("/<int:id>")
def obtener(id):
    return schema.dump(obtener_o_404(Producto, id, "El producto"))


@bp.post("")
@jwt_required()
def crear():
    datos = schema.load(datos_json())
    validar_categoria(datos)

    producto = Producto(**datos)
    db.session.add(producto)
    db.session.commit()
    return schema.dump(producto), 201


@bp.put("/<int:id>")
@jwt_required()
def actualizar(id):
    producto = obtener_o_404(Producto, id, "El producto")
    foto_anterior = producto.foto

    datos = schema.load(datos_json())
    validar_categoria(datos)

    asignar(producto, datos)
    db.session.commit()

    reemplazar_imagen(foto_anterior, producto.foto)
    return schema.dump(producto)


@bp.delete("/<int:id>")
@jwt_required()
def eliminar(id):
    producto = obtener_o_404(Producto, id, "El producto")

    en_combo = db.session.scalar(
        db.select(ComboDetalle.id).filter_by(producto_id=producto.id).limit(1)
    )
    if en_combo is not None:
        raise ErrorApi("No se puede eliminar porque forma parte de un combo.", 409)

    foto = producto.foto
    db.session.delete(producto)
    db.session.commit()

    borrar_imagen(foto)
    return "", 204
