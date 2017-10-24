# -*- coding: utf-8 -*-
# try something like
@auth.requires_login()
def index():
    "index del carrito"
    # creo una lista vacia en la sesion (para guardar los id de los articulos)
    if not session["carrito"]:
        session["carrito"] = []
    # si viene el id en el request, lo agrego a la session:
    if request.args:
        id_articulo = int(request.args[0])
        session["carrito"].append(id_articulo)
    # busco todos los articulos cuyo id esté en la sesion (carrito)
    datos_articulo=[]
    for id_articulo in session ["carrito"]:
        reg = db(db.articulo.id==id_articulo).select().first()
        datos_articulo.append(reg)
    return dict (da=datos_articulo)

@auth.requires_login()
def eliminar():
    if request.args:
        id_articulo = int(request.args[0])
        session["carrito"].remove(id_articulo)
    redirect(URL(c="carrito", f="index"))

@auth.requires_login()
def detalle():
    "detalle de la compra"
    result = mail.send(to=['storephone@gmail.com'],subject='Compra en StorePhone',reply_to='nogueralucasezequiel@gmail.com',message='Muchas Gracias por realizar tu compra en Store Phone, al correr de los dias se les detallara el estado de su compra')

    if session["carrito"]:
        # crear un registro para el pedido (completar datos generales: fecha, n fact, etc.)
        id_venta = db.ventas.insert(detalle="nuevo pedido!")
        # busco todos los articulos cuyo id esté en la sesion (carrito)
        datos_articulo=[]
        for id_articulo in session ["carrito"]:
            reg = db(db.articulo.id==id_articulo).select().first()
            datos_articulo.append(reg)
            db.ventas_por_articulo.insert(venta=id_venta, articulo=id_articulo)
        return dict (da=datos_articulo)

    
    return dict(result=result)


@auth.requires_login()
def confirmacion():
    "confirmacion de compra"
    return dict(message="")

@auth.requires_login()
def factura():
    "Factura de la compra"
    return dict(message="")
