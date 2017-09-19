@auth.requires_membership(role='Supervisor')
def listado_ventas():
    #LISTARA LAS VENTAS, QUE TENDRAN QUE SER CONFIRMADAS O DENEGADAS, DEPENDIENDO DEL STOCK VO, RE PIOLA VDAAAAAAAAAAAAAAAAA MI UÑAAA VOOO
    return dict(message="hello from ventas.py")
def reporte():
    "pagina de inicio del catalogo"
    estados_de_ventas=db().select(db.estados_de_ventas.ALL)
    return dict (ev=estados_de_ventas)
