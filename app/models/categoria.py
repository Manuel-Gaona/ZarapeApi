from app.extensions import db

# Un producto (y por lo tanto su categoría) es un alimento o una bebida
TIPOS_PRODUCTO = ["alimento", "bebida"]


class Categoria(db.Model):
    """Categoría de un producto: Tortas, Postres, Jugos, Refrescos..."""

    __tablename__ = "categorias"
    __table_args__ = (db.UniqueConstraint("nombre", "tipo"),)

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)

    productos = db.relationship("Producto", back_populates="categoria")
