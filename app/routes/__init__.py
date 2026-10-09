"""Rutas de la API, agrupadas en un blueprint por recurso.

Regla de acceso:
  - Consultar el menú (categorías, productos y combos) es público.
  - Todo lo demás requiere iniciar sesión (token JWT).
"""

from app.routes import (
    auth,
    categorias,
    combos,
    empleados,
    imagenes,
    productos,
    sucursales,
    usuarios,
)

BLUEPRINTS = [
    auth.bp,
    categorias.bp,
    combos.bp,
    empleados.bp,
    imagenes.bp,
    imagenes.bp_archivos,
    productos.bp,
    sucursales.bp,
    usuarios.bp,
]


def registrar_rutas(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

    @app.get("/api/salud")
    def salud():
        """Sirve para comprobar rápido que la API está encendida."""
        return {"estado": "ok"}
