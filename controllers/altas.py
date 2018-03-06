# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from altas.py")

#@auth.requires_membership(role='Administrador')
def alta_cliente():
    form=SQLFORM(db.clientes)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario correctamente cargado'
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)
@auth.requires_membership(role='Administrador')
def alta_proveedor():
    form=SQLFORM(db.proveedor)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario correctamente cargado'
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)
@auth.requires_membership(role='Administrador')
def alta_articulo():
    form=SQLFORM(db.articulo)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario correctamente cargado'
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)
