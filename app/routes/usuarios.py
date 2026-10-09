from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from app.extensions import db
from app.models import Usuario
from app.schemas import UsuarioSchema
from app.utils.consultas import datos_json, filtrar_por_texto, obtener_o_404
from app.utils.errores import ErrorApi

bp = Blueprint("usuarios", __name__, url_prefix="/api/usuarios")

schema = UsuarioSchema()


@bp.before_request
def exigir_sesion():
    """Todas las rutas de este blueprint requieren iniciar sesión."""
    verify_jwt_in_request()


def validar_nombre_disponible(nombre, id_actual=None):
    existente = db.session.scalar(db.select(Usuario).filter_by(nombre=nombre))
    if existente is not None and existente.id != id_actual:
        raise ErrorApi(
            "Revisa los datos del formulario.",
            409,
            {"nombre": ["Ya existe un usuario con ese nombre."]},
        )


@bp.get("")
def listar():
    consulta = db.select(Usuario).order_by(Usuario.nombre)
    consulta = filtrar_por_texto(consulta, request.args.get("buscar"), Usuario.nombre)
    return schema.dump(db.session.scalars(consulta), many=True)


@bp.post("")
def crear():
    datos = schema.load(datos_json())
    validar_nombre_disponible(datos["nombre"])

    usuario = Usuario(nombre=datos["nombre"])
    usuario.set_password(datos["password"])
    db.session.add(usuario)
    db.session.commit()
    return schema.dump(usuario), 201


@bp.put("/<int:id>")
def actualizar(id):
    usuario = obtener_o_404(Usuario, id, "El usuario")
    # Al editar, la contraseña es opcional: si no se envía, se conserva la actual
    datos = schema.load(datos_json(), partial=("password",))
    validar_nombre_disponible(datos["nombre"], id_actual=usuario.id)

    usuario.nombre = datos["nombre"]
    if datos.get("password"):
        usuario.set_password(datos["password"])
    db.session.commit()
    return schema.dump(usuario)


@bp.delete("/<int:id>")
def eliminar(id):
    usuario = obtener_o_404(Usuario, id, "El usuario")
    if usuario.id == int(get_jwt_identity()):
        raise ErrorApi("No puedes eliminar tu propio usuario.", 409)

    db.session.delete(usuario)
    db.session.commit()
    return "", 204
