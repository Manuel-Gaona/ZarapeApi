"""Comandos propios para la terminal:  flask <comando>"""

import os

import click


def registrar_comandos(app):
    @app.cli.command("seed")
    def seed():
        """Carga los datos de ejemplo y crea el usuario administrador."""
        from app.seeds import sembrar

        usuario = os.getenv("ADMIN_USUARIO", "admin")
        password = os.getenv("ADMIN_PASSWORD", "admin123")

        if sembrar(usuario, password):
            click.echo(f"Datos de ejemplo cargados. Usuario administrador: {usuario}")
        else:
            click.echo("La base de datos ya tiene datos; no se cargó nada.")
