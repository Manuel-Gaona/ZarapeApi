from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db
from app.models.base import FechasMixin


class Usuario(FechasMixin, db.Model):
    """Persona que puede iniciar sesión en el panel de administración."""

    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    # Nunca se guarda la contraseña, solo su hash
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
