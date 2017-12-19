# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)

db.define_table('clientes',
	db.Field('usuario','string'),
	db.Field('password','password'),
	db.Field('nombre','string'),
	db.Field('apellido','string'),
	db.Field('direccion','string'),
    db.Field('ciudad','string'),
	db.Field('dni','integer'),
	db.Field('cuil','string'),
    db.Field('sexo'),
                )

db.clientes.password.requires=IS_ALPHANUMERIC()
db.clientes.sexo.requires=IS_IN_SET(['Masculino','Femenino'])
#db.clientes.cuil.requires=IS_ALPHANUMERIC()

db.define_table('proveedor',
	db.Field('nombre','string'),
    db.Field('razon_social','string'),
	db.Field('direccion','string'),
    db.Field('ciudad','string'),
	db.Field('telefono','string'),
	db.Field('cuit','string'),
    )
db.proveedor.cuit.requires=IS_ALPHANUMERIC()

db.define_table('articulo',
	db.Field('id_articulo','id'),
    db.Field('proveedor',db.proveedor),
	db.Field('nombre','string'),
    db.Field('pantalla','string'),
    db.Field('procesador','string'),
	db.Field('camara_principal','string'),
    db.Field('camara_secundaria','string'),
    db.Field('red','string'),
    db.Field('frecuencia_gsm','string'),
    db.Field('frecuencia_wcdma','string'),
    db.Field('bateria','string'),
    db.Field('bateria_modo_stand_by','string'),
    db.Field('memoria_ram','string'),
    db.Field('memoria_interna','string'),
    db.Field('memoria_externa','string'),
    db.Field('bluetooth','string'),
    db.Field('marcacion_por_voz','string'),
    db.Field('linea','string'),
    db.Field('precio','float'),
	db.Field('fabricacion','date'),
	db.Field('marca','string'),
	db.Field('sistema_operativo','string'),
	db.Field('stock','integer'),
    db.Field('imagen','upload'),
	)

db.articulo.bluetooth.requires=IS_IN_SET(['Si','No'])
db.articulo.marcacion_por_voz.requires=IS_IN_SET(['Si','No'])                
db.articulo.linea.requires=IS_IN_SET(['Personal','Movistar','Claro','Libre'])
db.articulo.marca.requires=IS_IN_SET(['Samsung','LG','Motorola','Huawei','Noblex'])
db.articulo.proveedor.requires=IS_IN_DB(db,db.proveedor.id,'%(nombre)s')

db.define_table('compras',
    db.Field('N_Factura','integer'),
    db.Field('fecha','date'),
	db.Field('p_unitario','integer'),
    db.Field('proveedor',db.proveedor),
    db.Field('cantidad','integer'),
    db.Field('id_articulo',db.articulo),
    db.Field('total','integer'))
db.compras.proveedor.requires=IS_IN_DB(db,db.proveedor.id,'%(nombre)s')
db.compras.id_articulo.requires=IS_IN_DB(db,db.articulo.id,'%(nombre)s')

db.define_table('ventas',
    db.Field('fecha','date'),
    db.Field('N_Factura','integer'),
    db.Field('cliente',db.clientes),
    db.Field('p_unitario','integer'),
    db.Field('detalle','string'),
    db.Field('total','integer'),
    db.Field('articulo',db.articulo))

db.ventas.cliente.requires=IS_IN_DB(db,db.clientes.id,'%(nombre)s')
db.ventas.articulo.requires=IS_IN_DB(db,db.articulo.id,'%(nombre)s')

db.define_table('ventas_por_articulo',
    db.Field('venta',db.ventas),
    db.Field('articulo',db.articulo),
    db.Field('cantidad','integer'),
    db.Field('subtotal','integer'))

db.define_table('pedidos',
    db.Field('cliente',db.clientes),
    db.Field('articulo',db.articulo),
    db.Field('fecha','date'),
#   db.Field('estados',db.estados),
    db.Field('estado','string'),
    db.Field('progreso','integer'),
    db.Field('color','string'),
    db.Field('cantidad','integer'))

db.pedidos.articulo.requires=IS_IN_DB(db,db.articulo.id,'%(nombre)s')
db.pedidos.cliente.requires=IS_IN_DB(db,db.clientes.id,'%(nombre)s')
#db.pedidos.estados.requires=IS_IN_DB(db,db.estados.id,'%(nombre)s')


db.define_table('estados_de_ventas',
    db.Field('estado','string'),
    db.Field('progreso','integer'),
    db.Field('color','string'))


db.define_table('compras_por_articulo',
    db.Field('venta',db.compras),
    db.Field('articulo',db.articulo),
    db.Field('cantidad','integer'),
    db.Field('subtotal','integer'))
