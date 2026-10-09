"""Extensiones de Flask.

Se crean aquí (sin la app) y se conectan en `create_app`. Así cualquier
módulo puede importarlas sin provocar importaciones circulares.
"""

import sqlite3

from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, event
from sqlalchemy.engine import Engine

# Nombres fijos para índices y llaves: hace que las migraciones sean predecibles
CONVENCION_NOMBRES = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

db = SQLAlchemy(metadata=MetaData(naming_convention=CONVENCION_NOMBRES))
migrate = Migrate()
jwt = JWTManager()
cors = CORS()


@event.listens_for(Engine, "connect")
def activar_llaves_foraneas_sqlite(conexion, _):
    """SQLite ignora las llaves foráneas a menos que se activen en cada conexión."""
    if isinstance(conexion, sqlite3.Connection):
        cursor = conexion.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
