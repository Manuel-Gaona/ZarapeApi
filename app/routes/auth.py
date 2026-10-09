from flask import Blueprint
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from app.extensions import db
from app.models import Usuario
from app.schemas import LoginSchema, UsuarioSchema
from app.utils.consultas import datos_json, obtener_o_404
from app.utils.errores import ErrorApi

bp = Blueprint("auth", __name__, url_prefix="/api/auth")

login_schema = LoginSchema()
usuario_schema = UsuarioSchema()


@bp.post("/login")
def login():
    datos = login_schema.load(datos_json())

    usuario = db.session.scalar(db.select(Usuario).filter_by(nombre=datos["nombre"]))
    if usuario is None or not usuario.check_password(datos["password"]):
        # Mismo mensaje en ambos casos: no revela si el usuario existe
        raise ErrorApi("Usuario o contraseña incorrectos.", 401)

    token = create_access_token(identity=str(usuario.id))
    return {"token": token, "usuario": usuario_schema.dump(usuario)}


@bp.get("/perfil")
@jwt_required()
def perfil():
    """Devuelve el usuario dueño del token."""
    usuario = obtener_o_404(Usuario, int(get_jwt_identity()), "El usuario")
    return usuario_schema.dump(usuario)
