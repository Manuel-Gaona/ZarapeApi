from datetime import datetime, timezone

from app.extensions import db


def ahora():
    return datetime.now(timezone.utc)


class FechasMixin:
    """Agrega a un modelo las fechas de creación y de última modificación."""

    creado_en = db.Column(db.DateTime, default=ahora, nullable=False)
    actualizado_en = db.Column(db.DateTime, default=ahora, onupdate=ahora, nullable=False)
