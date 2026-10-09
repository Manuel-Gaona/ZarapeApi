from flask import Blueprint, request
from flask_jwt_extended import verify_jwt_in_request

from app.extensions import db
from app.models import Empleado
from app.models.empleado import PUESTOS
from app.schemas import EmpleadoSchema
from app.utils.consultas import asignar, datos_json, filtrar_por_texto, obtener_o_404

bp = Blueprint("empleados", __name__, url_prefix="/api/empleados")

schema = EmpleadoSchema()


@bp.before_request
def exigir_sesion():
    verify_jwt_in_request()


@bp.get("/puestos")
def puestos():
    """Opciones para la lista desplegable de puestos."""
    return PUESTOS


@bp.get("")
def listar():
    consulta = db.select(Empleado).order_by(Empleado.nombre)
    consulta = filtrar_por_texto(
        consulta,
        request.args.get("buscar"),
        Empleado.nombre,
        Empleado.apellido_paterno,
        Empleado.apellido_materno,
        Empleado.puesto,
    )
    return schema.dump(db.session.scalars(consulta), many=True)


@bp.post("")
def crear():
    empleado = Empleado(**schema.load(datos_json()))
    db.session.add(empleado)
    db.session.commit()
    return schema.dump(empleado), 201


@bp.put("/<int:id>")
def actualizar(id):
    empleado = obtener_o_404(Empleado, id, "El empleado")
    asignar(empleado, schema.load(datos_json()))
    db.session.commit()
    return schema.dump(empleado)


@bp.delete("/<int:id>")
def eliminar(id):
    empleado = obtener_o_404(Empleado, id, "El empleado")
    db.session.delete(empleado)
    db.session.commit()
    return "", 204
