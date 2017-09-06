# -*- coding: utf-8 -*-
# try something like

def index():
    "pagina de inicio del catalogo"
    datos_articulo=db().select(db.articulo.ALL).first()
    datos_articulo=db(db.articulo.id==1).select(db.articulo.ALL).first()
    return dict (x=datos_articulo)

def caracteristicas():
    "pagina caracteristicas de celulares"
    return dict(message="funcion  caracteristicas")

def comparacion():
    "pagina de comparacion entre celulares"
    return dict(message="funcion  comparacion")

def inicio():
    "pagina de inicio del catalogo"
    return dict(message="funcion  inicio")

def motorola():
    "pagina de catalogo discriminados por modelo motorola"
    return dict(message="funcion  motorola")

def samsung():
    "pagina de catalogo discriminados por modelo samsung"
    return dict(message="funcion  samsung")
