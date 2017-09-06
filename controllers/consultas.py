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
def mostrar():
    # obtengo el id de prodcuto desde la URL
    prod_id = request.args[0]
    # consultamos a la bd para que traiga el registro del primer producto:
    reg = db(db.articulo.id==prod_id).select(db.articulo.imagen).first()
    # obtenemos la imagen (nombre de archivo completo, stream=flujo de datos=archivo abierto -open-):
    (filename, stream) = db.articulo.imagen.retrieve(reg.imagen)
    # obtenemos extension original para determinar tipo de contenido:
    import os.path
    ext = os.path.splitext(filename)[1].lower()
    if ext in (".jpg", ".jpeg", ".face"):
        formato = "image/jpeg"
    elif ext in (".png"):
        formato = "image/png"
    response.headers['Content-Type'] = formato
    # devolver al navegador el contenido de la imagen
    return stream
auth.requires_membership(role='Administrador')
def reporte_ventas():
    return dict(message="reporte_ventas")
@auth.requires_membership(role='Administrador')
def lista_ventas():
    # obtenemos los criterios de busqueda y generamos el reporte
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    return dict(titulo="Listando Desde: %s Hasta: %s" % (desde, hasta))
