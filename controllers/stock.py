# -*- coding: utf-8 -*-
# try something like
@auth.requires_membership(role='Supervisor')
def listado():
    datos_articulo=db().select(db.articulo.ALL)
    return dict (da=datos_articulo)
