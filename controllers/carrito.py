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
    #for usuario_log in session ["comprador_log"]:
     #   reg = db(db.clientes.clientes_id==clientes_id).select().first()
    for id_articulo in session ["carrito"]:
        reg = db(db.articulo.id==id_articulo).select().first()
        datos_articulo.append(reg)
    return dict (da=datos_articulo,comprador_log=comprador_log)

@auth.requires_login()
def eliminar():
    if request.args:
        id_articulo = int(request.args[0])
        session["carrito"].remove(id_articulo)
    redirect(URL(c="carrito", f="index"))

@auth.requires_login()
def detalle():
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
    
@auth.requires_login()
def confirmacion():
    "confirmacion de compra"
    return dict(message="")

@auth.requires_login()
def factura():
    "Factura de la compra"
    return dict(message="")



def finalizarcompra():
    request.vars["id_clientes"]
    pedidos = db(db.clientes.clientes_id == session["id_clientes"] ).select().first()
    #id_clientes = session["id_clientes"]
    #reg_clientes = db(db.clientes.clientes_id==id_clientes).select().first()
    #reg_cliente = db((db.clientes.clientes_id==id_clientes)&(db.pedidos.articulo ==  db.articulo.id_articulo)).select(db.articulo.nombre,db.articulo.precio).first()
    #reg_cantidad = db((db.pedidos.id==id_pedidos)&(db.pedidos.articulo ==  db.articulo.id_articulo)).select(db.pedidos.cantidad).first()
    return dict (pedidos=pedidos)
