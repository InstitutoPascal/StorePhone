@auth.requires_membership(role='Supervisor')
def listado_ventas():
    #LISTARA LAS VENTAS, QUE TENDRAN QUE SER CONFIRMADAS O DENEGADAS, DEPENDIENDO DEL STOCK VO, RE PIOLA VDAAAAAAAAAAAAAAAAA MI UÑAAA VOOO
    return dict(message="hello from ventas.py")
