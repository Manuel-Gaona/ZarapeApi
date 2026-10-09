"""Modelos de la base de datos (una clase por tabla)."""

from app.models.categoria import Categoria
from app.models.combo import Combo, ComboDetalle
from app.models.empleado import Empleado
from app.models.producto import Producto
from app.models.sucursal import Sucursal
from app.models.usuario import Usuario

__all__ = [
    "Categoria",
    "Combo",
    "ComboDetalle",
    "Empleado",
    "Producto",
    "Sucursal",
    "Usuario",
]
