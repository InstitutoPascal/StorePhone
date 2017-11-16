@auth.requires_membership(role='Supervisor')
def listado_ventas():
    #LISTARA LAS VENTAS, QUE TENDRAN QUE SER CONFIRMADAS O DENEGADAS, DEPENDIENDO DEL STOCK 
    return dict(message="hello from ventas.py")
def reporte():
    "pagina de inicio del catalogo"
    ventas=db().select(db.ventas.ALL)
    return dict (v=ventas)
