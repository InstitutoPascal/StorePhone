# -*- coding: utf-8 -*-
# try something like
@auth.requires_login()
def index():
    "index del carrito"
    return dict(message="hello from carrito.py")

@auth.requires_login()
def detalle():
    "detalle de la compra"
    return dict(message="hello from carrito.py")

@auth.requires_login()
def confirmacion():
    "confirmacion de compra"
    return dict(message="hello from carrito.py")

@auth.requires_login()
def factura():
    "Factura de la compra"
    return dict(message="hello from carrito.py")
