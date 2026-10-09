"""Configuración de la aplicación.

Los valores sensibles se leen de variables de entorno (archivo .env) para
no escribirlos en el código.
"""

import os
from datetime import timedelta

from dotenv import load_dotenv

# Carpeta "api/"
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "clave-solo-para-desarrollo")

    # Base de datos
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///zarape.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Autenticación con JWT
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "clave-jwt-solo-para-desarrollo")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=8)

    # Frontends que pueden consumir la API
    CORS_ORIGINS = [
        origen.strip()
        for origen in os.getenv(
            "CORS_ORIGINS", "http://localhost:5173,http://localhost:4173"
        ).split(",")
    ]

    # Imágenes subidas
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    EXTENSIONES_IMAGEN = {"png", "jpg", "jpeg", "webp"}
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB por petición
