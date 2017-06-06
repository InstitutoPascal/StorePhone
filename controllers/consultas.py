# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from consultas.py")
@auth.requires_membership(role='Administrador')
def listado_clientes():
    datos_clientes=db().select(db.clientes.ALL)
    return dict (dc=datos_clientes)
@auth.requires_membership(role='Administrador')
def listado_proveedor():
    datos_proveedor=db().select(db.proveedor.ALL)
    return dict (dp=datos_proveedor)
@auth.requires_membership(role='Administrador')
def listado_articulo():
    datos_articulo=db().select(db.articulo.ALL)
    return dict (da=datos_articulo)
@auth.requires_membership(role='Administrador')
def reporte_ventas():
    return dict(message="reporte_ventas")
@auth.requires_membership(role='Administrador')
def lista_ventas():
    # obtenemos los criterios de busqueda y generamos el reporte
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    return dict(titulo="Listando Desde: %s Hasta: %s" % (desde, hasta))
