# -*- coding: utf-8 -*-
# try something like

def index():
    "pagina de inicio del catalogo"
    datos_articulo=db().select(db.articulo.ALL)
    return dict (da=datos_articulo)

def caracteristicas():
    "pagina caracteristicas de celulares"
    return dict(message="funcion  caracteristicas")

def comparacion():
    "pagina de comparacion entre celulares"
    return dict(message="funcion  comparacion")
