# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from consultas.py")
@auth.requires_membership(role='Gerente')
def listado_clientes():
    datos_clientes=db().select(db.clientes.ALL)
    return dict (dc=datos_clientes)
@auth.requires_membership(role='Gerente')
def listado_proveedor():
    datos_proveedor=db().select(db.proveedor.ALL)
    return dict (dp=datos_proveedor)
@auth.requires_membership(role='Gerente')
def listado_articulo():
    datos_articulo=db().select(db.articulo.ALL)
    return dict (da=datos_articulo)
