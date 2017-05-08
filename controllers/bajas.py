# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from bajas.py")
@auth.requires_membership(role='Administrador')
def borrar_cliente():
    # obtengo el primer argumento (ver URL)
    id_cliente = request.args[0]
    # busco y borro el registro
    db(db.clientes.id == id_cliente).delete()
    session.flash = "El cliente %s se borro exitosamente" % id_cliente
    # redirijo al usuario al listado
    redirect(URL(c="consultas", f="listado_clientes"))
@auth.requires_membership(role='Administrador')
def borrar_articulo():
    # obtengo el primer argumento (ver URL)
    id_arti = request.args[0]
    # busco y borro el registro
    db(db.articulo.id_articulo == id_arti).delete()
    session.flash = "El cliente %s se borro exitosamente" % id_arti
    # redirijo al usuario al listado
    redirect(URL(c="consultas", f="listado_articulo"))
@auth.requires_membership(role='Administrador')
def borrar_proveedor():
    # obtengo el primer argumento (ver URL)
    id_proveedor = request.args[0]
    # busco y borro el registro
    db(db.proveedor.id == id_proveedor).delete()
    session.flash = "El cliente %s se borro exitosamente" % id_proveedor
    # redirijo al usuario al listado
    redirect(URL(c="consultas", f="listado_proveedor"))
