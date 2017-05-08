# -*- coding: utf-8 -*-

@auth.requires_membership(role='Gerente')
def inicio_ventas():
    # definir los campos a obtener desde la base de datos:
    campos = db.clientes.id, db.clientes.nombre
    # definir la condición que deben cumplir los registros:
    criterio = db.clientes.id>0
    ##criterio &= db.cliente.condicion_frente_al_iva=="Responsable Inscripto"
    # ejecutar la consulta:
    lista_clientes = db(criterio).select(*campos)
    # revisar si la consulta devolvio registros:
    if not lista_clientes:
        mensaje = "No ha cargado clientes"
    else:
        mensaje = "Seleccione un cliente"
        ##primer_cliente = lista_clientes[0]
    return dict(message=mensaje, lista_clientes=lista_clientes)
@auth.requires_membership(role='Gerente')
def detalle_ventas():
    # si el usuario completo el formulario, extraigo los valores de los campos:
    if request.vars["boton_enviar"]:
        # obtengo los valores completados en el formulario
        id_cliente = request.vars["id_cliente"]
        fecha = request.vars["fecha"]
        nro_comprobante = request.vars["numero_comprobante"]
        # guardo los datos elegidos en la sesión
        session["id_cliente"] = id_cliente
        session["fecha"] = fecha
        session["nro_comprobante"] = nro_comprobante
        session["items_venta"] = []
    if request.vars["agregar_item"]:
        # obtengo los valores del formulario
        id_articulo = request.vars["id_producto"]
        cantidad = int(request.vars["cantidad"])
        precio = float(request.vars["precio"])
        item = {"id": id_articulo, "cantidad": cantidad}
        # busco en la base de datos el registro del producto seleccionado
        reg_producto = db(db.articulo.id_articulo==id_articulo).select().first()
        item["nombre"] = reg_producto.nombre
        item["precio"] = precio #reg_producto.precio
        # guardo el item en la sesión
        session["items_venta"].append(item)
    # busco en la base de datos al cliente para mostrar su info
    registros = db(db.clientes.id==session["id_cliente"]).select()
    reg_cliente = registros[0]
    lista_articulos = db(db.articulo.id_articulo>0).select()
    # le pasamos las variables a la vista para armar el html
    return dict(id_cliente=session["id_cliente"], fecha=session["fecha"], 
                nro_cbte=session["nro_comprobante"], 
                reg_cliente=reg_cliente, lista_productos=lista_articulos,
                items_venta=session["items_venta"])

@auth.requires_login()
def reporte_ventas():
    return dict(message="reporte_ventas")
@auth.requires_membership(role='Gerente')
def vista_previa():
    id_venta = request.args[0]
    reg_venta = db(db.ventas.id == id_venta).select().first()
    reg_cliente = db(db.clientes.id == reg_venta.cliente).select().first()
    # busco los datos de cada item vendido (id, cantidad, etc.) y del producto
    q = db.ventas_por_articulo.venta == id_venta
    q &= db.articulo.id_articulo == db.ventas_por_articulo.articulo 
    reg_detalle_ventas = db(q).select()
    return dict(message="vista_previa", 
                venta=reg_venta, 
                cliente=reg_cliente, 
                items=reg_detalle_ventas)
@auth.requires_membership(role='Gerente')
def borrar_item():
    # eliminar algo
    # request.vars tiene un diccionario con todos los parametros de la URL (luego del ?)
    id_a_borrar = request.vars["id"]
    #producto_a_borrar = request.vars["producto"]
    return dict(mensaje="Borrado registro del Item = %s" % (id_a_borrar))
@auth.requires_membership(role='Gerente')
def lista_ventas():
    # obtenemos los criterios de busqueda y generamos el reporte
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    return dict(titulo="Listando Desde: %s Hasta: %s" % (desde, hasta))
@auth.requires_membership(role='Gerente')
def guardado():
    # Agregar los registros a la base de datos:
    # encabezado:
    nuevo_id_venta = db.ventas.insert(
        cliente=session["id_cliente"],
        N_Factura=session["nro_comprobante"],
        fecha=session["fecha"],
        )
    # detalle (productos)
    for item in session["items_venta"]:
        db.ventas_por_articulo.insert(
            venta=nuevo_id_venta,
            articulo=item["id"],
            cantidad=item["cantidad"],
            subtotal=item["precio"]
            )
        # descontar el stock
        articulo = db(db.articulo.id==item["id"]).select().first()
        stock_actual = articulo.stock
        db(db.articulo.id==item["id"]).update(stock=stock_actual-item["cantidad"])
    return dict (mensaje= "Se guardo con exito el comprobante id=%s" % nuevo_id_venta,
                 id_venta=nuevo_id_venta)
@auth.requires_membership(role='Gerente')
def confirmar():
    reg_cliente = db(db.clientes.id==session["id_cliente"]).select().first()
    total = 0
    for item in session["items_venta"]:
        total += item["precio"] * item["cantidad"]
    return dict (mensaje= "Finalizar venta", 
                id_cliente=session["id_cliente"], fecha=session["fecha"], 
                nro_cbte=session["nro_comprobante"], 
                reg_cliente=reg_cliente, total=total)

@auth.requires_membership(role='Supervisor')
def listado_ventas():
    return dict(message="hello from carrito.py")
