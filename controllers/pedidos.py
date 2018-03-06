# -*- coding: utf-8 -*-
# intente algo como
import time
import datetime
from ConfigParser import SafeConfigParser

def ListaPedidos():
    datos_pedidos=db().select(db.pedidos.ALL)
    return dict (dp=datos_pedidos)

def editar_pedidos():
    # obtengo el primer argumento (ver URL)
    id_pedidos = request.args[0]
    # busco el registro en la bbdd
    pedidos =  db(db.pedidos.id == id_pedidos).select().first()
    # armo el formulario para modificar este registro:
    form=SQLFORM(db.pedidos, pedidos)
    if form.accepts(request.vars, session):
        session.flash = 'Formulario correctamente cargado'
        # redirijo al usuario al listado
        redirect(URL(c="pedidos", f="ListaPedidos"))
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)

def cargarfactura():
    import time
    id_pedidos = request.args[0]
    datos_pedidos = db(db.pedidos.id == id_pedidos).select().first()
    totalP = datos_pedidos.cantidad * datos_pedidos.articulo.precio
    db.ventas.insert(  cliente = datos_pedidos.cliente,
                       fecha= datos_pedidos.fecha,
                       cantidad = datos_pedidos.cantidad,
                       detalle = datos_pedidos.id,
                       total = totalP,
                       articulo = datos_pedidos.articulo.id_articulo)
    redirect(URL(c="pedidos", f="borrarpedido", args=(id_pedidos)))


def borrarpedido():
    # obtengo el primer argumento (ver URL)
    id_pedidos = request.args[0]
    # busco y borro el registro
    db(db.pedidos.id == id_pedidos).delete()
    session.flash = "El pedido %s se borro exitosamente" % id_pedidos
    # redirijo al usuario al listado
    redirect(URL(c="pedidos", f="ListaPedidos"))


def cambiarEstado():
    id_pedidos = session["id_pedidos"]
    reg_pedidos = db(db.pedidos.id==id_pedidos).select().first()
    db(db.pedidos.id==id_pedidos).update(estado=3)
    redirect(URL(c="pedidos", f="ListaPedidos"))

def pasaraentregado():
    id_pedidos = session["id_pedidos"]
    reg_pedidos = db(db.pedidos.id==id_pedidos).select().first()
    db(db.pedidos.id==id_pedidos).update(estado=4)
    redirect(URL(c="pedidos", f="ListaPedidos"))
