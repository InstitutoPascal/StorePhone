# -*- coding: utf-8 -*-
# intente algo como
def logueo():
    if "id_clientes" in request.vars:
        session["id_clientes"] = request.vars["id_clientes"]  # traer del form y guardo en la sesion
    pedidos = db(db.clientes.id == session["id_clientes"] ).select().first
    return dict(pedidos=pedidos)
