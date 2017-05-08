# -*- coding: utf-8 -*-
# try something like
@auth.requires_membership(role='Administrador')
def index():
    "Opcion para realizar una compra, se detallara un listado a completar"
    form=SQLFORM(db.compras)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario correctamente cargado'
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)

@auth.requires_membership(role='Administrador')
def listado():
    "Listado de las compras que se realizo"
    datos_compras=db().select(db.compras.ALL)
    return dict (c=datos_compras)

def subirComprobante():
    "Escanear la factura que se realizo la compra"
    return dict(message="hello from compras.py")
