"""Fábrica de la aplicación (patrón "application factory")."""

import os

from flask import Flask

from app.config import Config
from app.extensions import cors, db, jwt, migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # Extensiones
    db.init_app(app)
    # render_as_batch permite que SQLite modifique tablas en las migraciones
    migrate.init_app(app, db, render_as_batch=True)
    jwt.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": app.config["CORS_ORIGINS"]}})

    # Los modelos deben importarse para que las migraciones los detecten
    from app import models  # noqa: F401
    from app.commands import registrar_comandos
    from app.routes import registrar_rutas
    from app.utils.errores import registrar_manejadores_de_errores

    registrar_rutas(app)
    registrar_manejadores_de_errores(app)
    registrar_comandos(app)

    return app
