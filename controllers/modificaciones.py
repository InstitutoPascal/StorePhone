# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from modificaciones.py")
@auth.requires_membership(role='Administrador')
def editar_cliente():
    # obtengo el primer argumento (ver URL)
    id_cliente = request.args[0]
    # busco el registro en la bbdd
    cliente =  db(db.clientes.id == id_cliente).select().first()
    # armo el formulario para modificar este registro:
    form=SQLFORM(db.clientes, cliente)
    if form.accepts(request.vars, session):
        session.flash = 'Formulario correctamente cargado'
        # redirijo al usuario al listado
        redirect(URL(c="consultas", f="listado_clientes"))
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)
@auth.requires_membership(role='Administrador')
def editar_proveedor():
    # obtengo el primer argumento (ver URL)
    id_proveedor = request.args[0]
    # busco el registro en la bbdd
    proveedor =  db(db.proveedor.id == id_proveedor).select().first()
    # armo el formulario para modificar este registro:
    form=SQLFORM(db.proveedor, proveedor)
    if form.accepts(request.vars, session):
        session.flash = 'Formulario correctamente cargado'
        # redirijo al usuario al listado
        redirect(URL(c="consultas", f="listado_proveedor"))
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)
@auth.requires_membership(role='Administrador')
def editar_articulo():
    # obtengo el primer argumento (ver URL)
    id_articulo = request.args[0]
    # busco el registro en la bbdd
    articulo =  db(db.articulo.id == id_articulo).select().first()
    # armo el formulario para modificar este registro:
    form=SQLFORM(db.articulo, articulo)
    if form.accepts(request.vars, session):
        session.flash = 'Formulario correctamente cargado'
        # redirijo al usuario al listado
        redirect(URL(c="consultas", f="listado_articulo"))
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)
