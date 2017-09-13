# -*- coding: utf-8 -*-
# try something like

def index():
    "pagina de inicio del catalogo"
    datos_articulo=db().select(db.articulo.ALL)
    return dict (da=datos_articulo)
