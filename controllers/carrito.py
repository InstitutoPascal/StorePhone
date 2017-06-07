# -*- coding: utf-8 -*-
# try something like
@auth.requires_login()
def index():
    "index del carrito"
    return dict(message="hello from carrito.py")

@auth.requires_login()
def detalle():
    "detalle de la compra"
    result = mail.send(to=['storephone@gmail.com'],subject='Compra en StorePhone',reply_to='nogueralucasezequiel@gmail.com',message='Muchas Gracias por realizar tu compra en Store Phone, al correr de los dias se les detallara el estado de su compra')
    return dict(result=result)


@auth.requires_login()
def confirmacion():
    "confirmacion de compra"
    return dict(message="")

@auth.requires_login()
def factura():
    "Factura de la compra"
    return dict(message="")
