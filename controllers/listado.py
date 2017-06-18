# -*- coding: utf-8 -*-

############################ C L I E N T E S ####################################
def clientes_por_ciudad():
    subtitulo=T('Listado de Clientes por Ciudad')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Ciudad:",INPUT(_type="text",_name="ciudad",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.clientes.ciudad!=form.vars.ciudad).count()==0:
            form.errors.codigo="El nombre ingresado no está en la base de datos"
            response.flash = 'El nombre ingresado no está en la base de datos'
        else:
            listado =db(db.clientes.ciudad==form.vars.ciudad).select(db.clientes.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('DNI',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('APELLIDO',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('NOMBRE',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH(i,' CLIENTE',_style='width:120px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'))),
            *[TR(TD(rows.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(rows.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(rows.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for rows in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)

def clientes_por_dni():
    subtitulo=T('Listado de Clientes por DNI')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("DNI:",INPUT(_type="text",_name="dni",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.clientes.dni!=form.vars.dni).count()==0:
            form.errors.codigo="El nombre ingresado no está en la base de datos"
            response.flash = 'El nombre ingresado no está en la base de datos'
        else:
            listado =db(db.clientes.dni==int(form.vars.dni)).select(db.clientes.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('DNI',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('APELLIDO',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('NOMBRE',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH(i,' CLIENTE',_style='width:120px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'))),
            *[TR(TD(rows.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(rows.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(rows.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for rows in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)

################################# A R T I C U L O S ################################################

def articulos_por_codigo():
    subtitulo=T('Listado de Articulos por codigo')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Numero articulo:",INPUT(_type="text",_name="codigo",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.articulo.id_articulo!=form.vars.codigo).count()==0:
            form.errors.codigo="El nombre ingresado no está en la base de datos"
            response.flash = 'El nombre ingresado no está en la base de datos'
        else:
            listado =db(db.articulo.id_articulo==int(form.vars.codigo)).select(db.articulo.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('NOMBRE',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('MARCA',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('LINEA',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH(i,' ARTICULO',_style='width:120px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'))),
            *[TR(TD(rows.nombre,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(rows.marca,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(rows.linea,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for rows in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def articulos_por_varios_nombres():
    subtitulo=T('Listado de Articulos por Varios Nombres')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Nombre de Articulo:",INPUT(_type="text",_name="names",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.articulo.nombre!=form.vars.names).count()==0:
            form.errors.codigo="El nombre ingresado no está en la base de datos"
            response.flash = 'El nombre ingresado no está en la base de datos'
        else:
            listado =db(db.articulo.nombre==form.vars.names).select(db.articulo.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('NOMBRE',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('MARCA',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('LINEA',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH(i,' ARTICULOS',_style='width:120px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'))),
            *[TR(TD(rows.nombre,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(rows.marca,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(rows.linea,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for rows in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def articulos_por_1_nombre():
    subtitulo=T('Listado de Articulos por 1 Nombre')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Nombre de Articulo:",INPUT(_type="text",_name="names",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.articulo.nombre!=form.vars.names).count()==0:
            form.errors.codigo="El nombre ingresado no está en la base de datos"
            response.flash = 'El nombre ingresado no está en la base de datos'
        else:
            listado =db(db.articulo.nombre==form.vars.names).select(db.articulo.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('NOMBRE',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('MARCA',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('LINEA',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH(i,' ARTICULO',_style='width:120px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'))),
            *[TR(TD(rows.nombre,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(rows.marca,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(rows.linea,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for rows in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)

##################################### P R O V E E D O R E S #####################################################

def proveedor_por_codigo():
    subtitulo=T('Listado de Proveedores por codigo')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Numero Proveedor:",INPUT(_type="text",_name="code",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.proveedor.id!=form.vars.code).count()==0:
            form.errors.codigo="El nombre ingresado no está en la base de datos"
            response.flash = 'El nombre ingresado no está en la base de datos'
        else:
            listado =db(db.proveedor.id==int(form.vars.code)).select(db.proveedor.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('NOMBRE',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('DIRECCION',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('CUIT',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH(i,' PROVEEDOR',_style='width:120px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'))),
            *[TR(TD(rows.nombre,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(rows.direccion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(rows.cuit,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for rows in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)

def proveedor_por_razon_social():
    subtitulo=T('Listado de Proveedores por Razón Social')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Razón Social:",INPUT(_type="text",_name="rs",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.proveedor.razon_social!=form.vars.rs).count()==0:
            form.errors.codigo="El nombre ingresado no está en la base de datos"
            response.flash = 'El nombre ingresado no está en la base de datos'
        else:
            listado =db(db.proveedor.razon_social==form.vars.rs).select(db.proveedor.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('NOMBRE',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('DIRECCION',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('CIUDAD',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH(i,' PROVEEDOR',_style='width:120px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'))),
            *[TR(TD(rows.nombre,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(rows.direccion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(rows.ciudad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for rows in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)
def proveedor_por_ciudad():
    subtitulo=T('Listado de Proveedores por Ciudad')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Ciudad:",INPUT(_type="text",_name="city",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.proveedor.ciudad!=form.vars.city).count()==0:
            form.errors.codigo="El nombre ingresado no está en la base de datos"
            response.flash = 'El nombre ingresado no está en la base de datos'
        else:
            listado =db(db.proveedor.ciudad==form.vars.city).select(db.proveedor.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('NOMBRE',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('DIRECCION',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH('CIUDAD',_style='width:200px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'),TH(i,' PROVEEDOR',_style='width:120px; color:#000; background: #ADD6EF; border: 2px solid #cdcdcd'))),
            *[TR(TD(rows.nombre,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(rows.direccion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(rows.ciudad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for rows in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)
