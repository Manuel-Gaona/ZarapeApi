from app.extensions import db
from app.models.base import FechasMixin


class Producto(FechasMixin, db.Model):
    """Alimento o bebida del menú.

    Ambos tienen exactamente los mismos datos, por eso comparten tabla y se
    distinguen con la columna `tipo` ("alimento" o "bebida").
    """

    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False, index=True)
    nombre = db.Column(db.String(120), nullable=False)
    descripcion = db.Column(db.Text, nullable=False, default="")
    foto = db.Column(db.String(255))
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id"), nullable=False)

    categoria = db.relationship("Categoria", back_populates="productos")
