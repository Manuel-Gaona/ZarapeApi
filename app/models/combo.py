from app.extensions import db
from app.models.base import FechasMixin


class Combo(FechasMixin, db.Model):
    """Paquete de productos que se vende a un precio especial."""

    __tablename__ = "combos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    descripcion = db.Column(db.Text, nullable=False, default="")
    foto = db.Column(db.String(255))
    precio = db.Column(db.Numeric(10, 2), nullable=False)

    # Al borrar un combo (o quitarle un detalle) se borran sus detalles
    detalles = db.relationship(
        "ComboDetalle",
        back_populates="combo",
        cascade="all, delete-orphan",
        order_by="ComboDetalle.id",
    )


class ComboDetalle(db.Model):
    """Un producto dentro de un combo y cuántas piezas incluye."""

    __tablename__ = "combo_detalles"

    id = db.Column(db.Integer, primary_key=True)
    combo_id = db.Column(db.Integer, db.ForeignKey("combos.id"), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False, default=1)

    combo = db.relationship("Combo", back_populates="detalles")
    producto = db.relationship("Producto")
