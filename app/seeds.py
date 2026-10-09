"""Datos de ejemplo (los mismos que aparecen en los mockups).

Se cargan con el comando:  flask seed
"""

import os

from app.config import BASE_DIR
from app.extensions import db
from app.models import Categoria, Combo, ComboDetalle, Empleado, Producto, Sucursal, Usuario
from app.utils.imagenes import copiar_imagen

CARPETA_IMAGENES = os.path.join(BASE_DIR, "seed", "imagenes")

EMPLEADOS = [
    # (nombre, apellido paterno, apellido materno, puesto)
    ("Juan Miguel", "Partida", "Hernández", "Cocinero"),
    ("Juan Luis", "Herrera", "Martínez", "Administrador"),
    ("Luis Ernesto", "Sandoval", "Ramírez", "Cocinero"),
]

SUCURSALES = [
    {
        "nombre": "El Zarape Av. Omega",
        "calle": "Valle de Yuca",
        "numero": "256A",
        "colonia": "Valle del Maguey",
        "ciudad": "León",
        "estado": "Guanajuato",
        "codigo_postal": "37545",
        "latitud": "21° 07' 19'' N",
        "longitud": "101° 40' 58'' O",
        "foto": "sucursal-omega.jpg",
        "url": "https://www.zarape.com/sucursal-omega",
        "hora_apertura": "09:00",
        "hora_cierre": "19:00",
    },
    {
        "nombre": "El Zarape Av. Insurgentes",
        "calle": "Valle de San Luis",
        "numero": "258",
        "colonia": "Las Peras",
        "ciudad": "Silao",
        "estado": "Guanajuato",
        "codigo_postal": "36100",
        "latitud": "20° 56' 37'' N",
        "longitud": "101° 25' 42'' O",
        "foto": "sucursal-insurgentes.jpg",
        "url": "https://www.zarape.com/sucursal-insurgentes",
        "hora_apertura": "09:00",
        "hora_cierre": "18:00",
    },
    {
        "nombre": "El Zarape Av. Poniente",
        "calle": "Valle del Verde",
        "numero": "265",
        "colonia": "Los Limones",
        "ciudad": "Salamanca",
        "estado": "Guanajuato",
        "codigo_postal": "36700",
        "latitud": "20° 34' 14'' N",
        "longitud": "101° 11' 50'' O",
        "foto": "sucursal-poniente.jpg",
        "url": "https://www.zarape.com/sucursal-poniente",
        "hora_apertura": "09:00",
        "hora_cierre": "18:00",
    },
]

# (nombre, categoría, precio, imagen, descripción)
ALIMENTOS = [
    ("Chile Relleno con crema y granada", "Platillos", 90, "chile-relleno.jpg",
     "Chile poblano relleno, bañado en crema de nuez y granada."),
    ("Plato de mole con pollo", "Platillos", 120, "mole-con-pollo.jpg",
     "Pieza de pollo cubierta con mole poblano y ajonjolí."),
    ("Orden de 4 flautas de pollo", "Antojitos", 90, "flautas.jpg",
     "Tortillas doradas rellenas de pollo, con lechuga, crema y queso."),
    ("Huarache con chorizo", "Antojitos", 70, "huarache.jpg",
     "Masa de maíz con frijoles, chorizo, lechuga, queso y salsa."),
    ("Elote con chile", "Antojitos", 30, "elote.jpg",
     "Elote cocido con mayonesa, queso y chile en polvo."),
    ("Enchiladas rojas", "Platillos", 70, "enchiladas.jpg",
     "Tortillas bañadas en salsa roja con queso, crema y cebolla."),
    ("Orden de 3 burritos", "Antojitos", 170, "burritos.jpg",
     "Tortillas de harina rellenas de carne, frijoles y verduras."),
    ("Pambazo con chorizo", "Tortas", 70, "pambazo.jpg",
     "Pan bañado en salsa guajillo, relleno de papa con chorizo."),
    ("Orden de 3 volcanes", "Antojitos", 60, "volcanes.jpg",
     "Tostadas con queso fundido y carne asada."),
    ("Quesadillas doradas", "Antojitos", 35, "quesadillas.jpg",
     "Quesadillas fritas con crema, queso y salsa."),
    ("Gorditas de deshebrada", "Antojitos", 70, "gorditas.jpg",
     "Gorditas de maíz rellenas de carne deshebrada."),
    ("Sopes con frijol y picadillo", "Antojitos", 35, "sopes.jpg",
     "Sopes de maíz con frijoles, picadillo, queso y crema."),
    ("Torta de Huevo con Chorizo", "Tortas", 40, "torta-huevo-chorizo.jpg",
     "Pan bolillo con huevo revuelto y chorizo, frijoles, queso, aguacate, "
     "jitomate, cebolla y mayonesa."),
    ("Ensalada de Jícama y Naranja", "Ensaladas", 30, "ensalada-jicama.jpg",
     "Jícama en tiras con gajos de naranja, pepino, cebolla morada y frutos "
     "rojos, aderezada con jugo de limón y chile en polvo."),
    ("Arroz con leche", "Postres", 25, "arroz-con-leche.jpg",
     "Arroz cocido en leche azucarada con canela y vainilla, espolvoreado con "
     "canela en polvo. Dulce y cremoso, se disfruta caliente o frío."),
]

BEBIDAS = [
    ("Jugo de naranja 600ml", "Jugos", 45, "jugo-naranja.jpg",
     "Jugo de naranja fresco exprimido, dulce y cítrico."),
    ("Jugo de betabel 600ml", "Jugos", 35, "jugo-betabel.jpg",
     "Jugo natural de betabel con naranja y zanahoria."),
    ("Jugo de zanahoria 600ml", "Jugos", 40, "jugo-zanahoria.jpg",
     "Jugo natural de zanahoria recién hecho."),
    ("Jugo de manzana", "Jugos", 55, "jugo-manzana.jpg",
     "Jugo natural de manzana."),
    ("Coca-cola 600ml", "Refrescos", 24, "coca-cola.jpg", "Refresco de cola."),
    ("Refresco Sprite 600ml", "Refrescos", 19, "sprite.jpg", "Refresco de lima-limón."),
    ("Sidral Mundet 600ml", "Refrescos", 20, "sidral-mundet.jpg", "Refresco de manzana."),
    ("Refresco Fanta 600ml", "Refrescos", 22, "fanta.jpg", "Refresco de naranja."),
    ("Cerveza Modelo 355ml", "Cervezas", 35, "cerveza-modelo.jpg", "Cerveza clara."),
    ("Cerveza Heineken 600ml", "Cervezas", 30, "cerveza-heineken.jpg", "Cerveza clara."),
    ("Cerveza Tecate 325ml", "Cervezas", 45, "cerveza-tecate.jpg", "Cerveza clara."),
    ("Cerveza Corona 473ml", "Cervezas", 40, "cerveza-corona.jpg", "Cerveza clara."),
    ("Café de Olla", "Cafés", 25, "cafe-de-olla.jpg",
     "Café tradicional mexicano con café de grano, canela y piloncillo."),
    ("Agua de Jamaica", "Aguas", 20, "agua-de-jamaica.jpg",
     "Infusión fría de flores de Jamaica, endulzada con azúcar."),
]

# (nombre, precio, imagen, [(cantidad, nombre del producto)])
COMBOS = [
    ("San Lunes", 450, "combo-san-lunes.jpg", [
        (2, "Plato de mole con pollo"),
        (2, "Orden de 4 flautas de pollo"),
        (2, "Refresco Sprite 600ml"),
    ]),
    ("San Martes", 180, "combo-san-martes.jpg", [
        (1, "Chile Relleno con crema y granada"),
        (1, "Huarache con chorizo"),
        (1, "Jugo de naranja 600ml"),
    ]),
    ("San Miércoles", 300, "combo.jpg", [
        (2, "Enchiladas rojas"),
        (2, "Pambazo con chorizo"),
        (2, "Coca-cola 600ml"),
    ]),
    ("Jueves Norteño", 170, "combo-san-jueves.jpg", [
        (4, "Sopes con frijol y picadillo"),
        (1, "Elote con chile"),
        (1, "Sidral Mundet 600ml"),
    ]),
    ("San Viernes", 560, "combo.jpg", [
        (2, "Orden de 3 volcanes"),
        (4, "Quesadillas doradas"),
        (6, "Cerveza Corona 473ml"),
    ]),
    ("Vuelve A La Vida", 400, "combo.jpg", [
        (2, "Orden de 3 burritos"),
        (1, "Gorditas de deshebrada"),
        (1, "Refresco Fanta 600ml"),
    ]),
    ("Por Fin Sábado", 200, "combo.jpg", [
        (2, "Orden de 3 volcanes"),
        (2, "Quesadillas doradas"),
        (2, "Cerveza Heineken 600ml"),
    ]),
    ("Pareja Enamorada", 450, "combo.jpg", [
        (2, "Plato de mole con pollo"),
        (2, "Elote con chile"),
        (4, "Cerveza Tecate 325ml"),
    ]),
    ("Dominguero", 800, "combo.jpg", [
        (4, "Chile Relleno con crema y granada"),
        (12, "Cerveza Corona 473ml"),
    ]),
]


def _imagen(nombre_archivo):
    """Copia la imagen de ejemplo a la carpeta de subidas y devuelve su ruta."""
    return copiar_imagen(os.path.join(CARPETA_IMAGENES, nombre_archivo))


def _crear_productos(tipo, filas):
    """Crea los productos (y sus categorías) y los devuelve por nombre."""
    categorias = {}
    productos = {}
    for nombre, categoria, precio, imagen, descripcion in filas:
        if categoria not in categorias:
            categorias[categoria] = Categoria(nombre=categoria, tipo=tipo)
        productos[nombre] = Producto(
            tipo=tipo,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            foto=_imagen(imagen),
            categoria=categorias[categoria],
        )
    db.session.add_all(productos.values())
    return productos


def sembrar(usuario_admin, password_admin):
    """Llena la base de datos. Devuelve False si ya tenía datos."""
    if db.session.scalar(db.select(Usuario.id).limit(1)) is not None:
        return False

    admin = Usuario(nombre=usuario_admin)
    admin.set_password(password_admin)
    db.session.add(admin)

    for nombre, paterno, materno, puesto in EMPLEADOS:
        db.session.add(
            Empleado(
                nombre=nombre,
                apellido_paterno=paterno,
                apellido_materno=materno,
                puesto=puesto,
            )
        )

    for datos in SUCURSALES:
        db.session.add(Sucursal(**{**datos, "foto": _imagen(datos["foto"])}))

    productos = {
        **_crear_productos("alimento", ALIMENTOS),
        **_crear_productos("bebida", BEBIDAS),
    }

    for nombre, precio, imagen, contenido in COMBOS:
        descripcion = "Incluye " + ", ".join(
            f"{cantidad} {producto}" for cantidad, producto in contenido
        ) + "."
        db.session.add(
            Combo(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                foto=_imagen(imagen),
                detalles=[
                    ComboDetalle(producto=productos[producto], cantidad=cantidad)
                    for cantidad, producto in contenido
                ],
            )
        )

    db.session.commit()
    return True
