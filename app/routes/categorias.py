from flask import Blueprint, request

from app.extensions import db
from app.models import Categoria
from app.schemas import CategoriaSchema

bp = Blueprint("categorias", __name__, url_prefix="/api/categorias")

schema = CategoriaSchema()


@bp.get("")
def listar():
    """Lista las categorías. Con ?tipo=alimento o ?tipo=bebida filtra por tipo."""
    consulta = db.select(Categoria).order_by(Categoria.nombre)

    tipo = request.args.get("tipo")
    if tipo:
        consulta = consulta.where(Categoria.tipo == tipo)

    return schema.dump(db.session.scalars(consulta), many=True)
