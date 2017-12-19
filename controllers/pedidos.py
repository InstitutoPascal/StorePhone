# -*- coding: utf-8 -*-
# intente algo como
def ListaPedidos():
    datos_pedidos=db().select(db.pedidos.ALL)
    return dict (dp=datos_pedidos)
