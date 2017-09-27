# -*- coding: utf-8 -*-

import datetime
from ConfigParser import SafeConfigParser

def obtener_cae():
    from pyafipws.wsaa import WSAA
    from pyafipws.wsfev1 import WSFEv1

    # web service de factura electronica:
    wsfev1 = WSFEv1()
    wsfev1.LanzarExcepciones = True

    # obteniendo el TA para pruebas
    ta = WSAA().Autenticar("wsfe", "/home/leo/pyafipws/reingart.crt",
                                   "/home/leo/pyafipws/reingart.key", debug=True)
    wsfev1.SetTicketAcceso(ta)
    wsfev1.Cuit = "20267565393"

    ok = wsfev1.Conectar()

    tipo_cbte = 6
    punto_vta = 4001
    cbte_nro = long(wsfev1.CompUltimoAutorizado(tipo_cbte, punto_vta) or 0)
    fecha = datetime.datetime.now().strftime("%Y%m%d")
    concepto = 1
    tipo_doc = 80 # 80: CUIT, 96: DNI
    nro_doc = "30500010912" # del cliente
    cbt_desde = cbte_nro + 1; cbt_hasta = cbte_nro + 1
    imp_total = "222.00"
    imp_tot_conc = "0.00"
    imp_neto = "200.00"
    imp_iva = "21.00"
    imp_trib = "1.00"
    imp_op_ex = "0.00"
    fecha_cbte = fecha
    # Fechas del per�odo del servicio facturado y vencimiento de pago:
    if concepto > 1:
        fecha_venc_pago = fecha
        fecha_serv_desde = fecha
        fecha_serv_hasta = fecha
    else:
        fecha_venc_pago = fecha_serv_desde = fecha_serv_hasta = None
    moneda_id = 'PES'
    moneda_ctz = '1.000'

    wsfev1.CrearFactura(concepto, tipo_doc, nro_doc, 
                tipo_cbte, punto_vta, cbt_desde, cbt_hasta , 
                imp_total, imp_tot_conc, imp_neto,
                imp_iva, imp_trib, imp_op_ex, fecha_cbte, fecha_venc_pago, 
                fecha_serv_desde, fecha_serv_hasta, #--
                moneda_id, moneda_ctz)

    # otros tributos:
    tributo_id = 99
    desc = 'Impuesto Municipal Matanza'
    base_imp = None
    alic = None
    importe = 1
    wsfev1.AgregarTributo(tributo_id, desc, base_imp, alic, importe)

    # subtotales por alicuota de IVA:
    iva_id = 3 # 0%
    base_imp = 100    # neto al 0%
    importe = 0
    wsfev1.AgregarIva(iva_id, base_imp, importe)

    # subtotales por alicuota de IVA:
    iva_id = 5 # 21%
    base_imp = 100   # neto al 21%
    importe = 21     # iva liquidado al 21%
    wsfev1.AgregarIva(iva_id, base_imp, importe)

    wsfev1.CAESolicitar()

    print "Nro. Cbte. desde-hasta", wsfev1.CbtDesde, wsfev1.CbtHasta
    print "Resultado", wsfev1.Resultado
    print "Reproceso", wsfev1.Reproceso
    print "CAE", wsfev1.CAE
    print "Vencimiento", wsfev1.Vencimiento
    print "Observaciones", wsfev1.Obs

    session.cae = wsfev1.CAE
    response.view = "generic.html"
    return {"Nro. Cbte. desde-hasta": wsfev1.CbtDesde,
            "Resultado": wsfev1.Resultado,
            "Reproceso": wsfev1.Reproceso,
            "CAE": wsfev1.CAE,
            "Vencimiento": wsfev1.Vencimiento,
            "Observaciones": wsfev1.Obs,
          }
    

def generar_pdf(): 
    CONFIG_FILE = "/home/leo/pyafipws/rece.ini"

    config = SafeConfigParser()
    config.read(CONFIG_FILE)
    conf_fact = dict(config.items('FACTURA'))
    conf_pdf = dict(config.items('PDF'))

    from pyafipws.pyfepdf import FEPDF
    fepdf = FEPDF()

    # cargo el formato CSV por defecto (factura.csv)
    fepdf.CargarFormato(conf_fact.get("formato", "factura.csv"))

    # establezco formatos (cantidad de decimales) según configuración:
    fepdf.FmtCantidad = conf_fact.get("fmt_cantidad", "0.2")
    fepdf.FmtPrecio = conf_fact.get("fmt_precio", "0.2")


    # creo una factura de ejemplo
    HOMO = True

    # datos generales del encabezado:
    tipo_cbte = 1
    punto_vta = 4000
    fecha = datetime.datetime.now().strftime("%Y%m%d")
    concepto = 3
    tipo_doc = 80; nro_doc = "30000000007"
    cbte_nro = 12345678
    imp_total = "127.00"
    imp_tot_conc = "3.00"
    imp_neto = "100.00"
    imp_iva = "21.00"
    imp_trib = "1.00"
    imp_op_ex = "2.00"
    imp_subtotal = "105.00"
    fecha_cbte = fecha
    fecha_venc_pago = fecha
    # Fechas del período del servicio facturado (solo si concepto> 1)
    fecha_serv_desde = fecha
    fecha_serv_hasta = fecha
    # campos p/exportación (ej): DOL para USD, indicando cotización:
    moneda_id = 'PES'
    moneda_ctz = 1
    incoterms = 'FOB'                   # solo exportación
    idioma_cbte = 1                     # 1: es, 2: en, 3: pt

    # datos adicionales del encabezado:
    nombre_cliente = 'Juan Perez'
    domicilio_cliente = 'Rua 76 km 34.5 Alagoas'
    pais_dst_cmp = 212                  # 200: Argentina, ver tabla
    id_impositivo = 'PJ54482221-l'      # cat. iva (mercado interno)
    forma_pago = '30 dias'

    obs_generales = "Observaciones Generales<br/>linea2<br/>linea3"
    obs_comerciales = "Observaciones Comerciales<br/>texto libre"

    # datos devueltos por el webservice (WSFEv1, WSMTXCA, etc.):
    motivo_obs = "Factura individual, DocTipo: 80, DocNro 30000000007 no se encuentra registrado en los padrones de AFIP."
    cae = session.cae
    fch_venc_cae = "20110320"

    fepdf.CrearFactura(concepto, tipo_doc, nro_doc, tipo_cbte, punto_vta,
        cbte_nro, imp_total, imp_tot_conc, imp_neto,
        imp_iva, imp_trib, imp_op_ex, fecha_cbte, fecha_venc_pago, 
        fecha_serv_desde, fecha_serv_hasta, 
        moneda_id, moneda_ctz, cae, fch_venc_cae, id_impositivo,
        nombre_cliente, domicilio_cliente, pais_dst_cmp, 
        obs_comerciales, obs_generales, forma_pago, incoterms, 
        idioma_cbte, motivo_obs)

    # completo campos extra del encabezado:
    ok = fepdf.EstablecerParametro("localidad_cliente", "Hurlingham")
    ok = fepdf.EstablecerParametro("provincia_cliente", "Buenos Aires")

    # imprimir leyenda "Comprobante Autorizado" (constatar con WSCDC!)
    ok = fepdf.EstablecerParametro("resultado", "A")

    # tributos adicionales:
    tributo_id = 99
    desc = 'Impuesto Municipal Matanza'
    base_imp = "100.00"
    alic = "1.00"
    importe = "1.00"
    fepdf.AgregarTributo(tributo_id, desc, base_imp, alic, importe)

    tributo_id = 4
    desc = 'Impuestos Internos'
    base_imp = None
    alic = None
    importe = "0.00"
    fepdf.AgregarTributo(tributo_id, desc, base_imp, alic, importe)

    # subtotales por alícuota de IVA:
    iva_id = 5 # 21%
    base_imp = 100
    importe = 21
    fepdf.AgregarIva(iva_id, base_imp, importe)

    # detalle de artículos:
    u_mtx = 123456
    cod_mtx = 1234567890123
    codigo = "P0001"
    ds = "Descripcion del producto P0001\n"
    qty = 1.00
    umed = 7
    if tipo_cbte in (1, 2, 3, 4, 5, 34, 39, 51, 52, 53, 54, 60, 64):
        # discriminar IVA si es clase A / M
        precio = 110.00
        imp_iva = 23.10
    else:
        # no discriminar IVA si es clase B (importe final iva incluido)
        precio = 133.10
        imp_iva = None
    bonif = 0.00
    iva_id = 5
    importe = 133.10
    despacho = u'Nº 123456'
    dato_a = "Dato A"
    fepdf.AgregarDetalleItem(u_mtx, cod_mtx, codigo, ds, qty, umed, 
            precio, bonif, iva_id, imp_iva, importe, despacho, dato_a)

    # descuento general (a tasa 21%):
    u_mtx = cod_mtx = codigo = None
    ds = u"Bonificación/Descuento 10%"
    qty = precio = bonif = None
    umed = 99
    iva_id = 5
    if tipo_cbte in (1, 2, 3, 4, 5, 34, 39, 51, 52, 53, 54, 60, 64):
        # discriminar IVA si es clase A / M
        imp_iva = -2.21
    else:
        imp_iva = None
    importe = -12.10
    fepdf.AgregarDetalleItem(u_mtx, cod_mtx, codigo, ds, qty, umed, 
            precio, bonif, iva_id, imp_iva, importe, "")

    # descripción (sin importes ni cantidad):
    u_mtx = cod_mtx = codigo = None
    qty = precio = bonif = iva_id = imp_iva = importe = None
    umed = 0
    ds = u"Descripción Ejemplo"
    fepdf.AgregarDetalleItem(u_mtx, cod_mtx, codigo, ds, qty, umed, 
            precio, bonif, iva_id, imp_iva, importe, "")

    # completo campos personalizados de la plantilla:
    fepdf.AgregarDato("custom-nro-cli", "Cod.123")
    fepdf.AgregarDato("custom-pedido", "1234")
    fepdf.AgregarDato("custom-remito", "12345")
    fepdf.AgregarDato("custom-transporte", "Camiones Ej.")
    print "Prueba!"
    
    # datos fijos:
    for k, v in conf_pdf.items():
        fepdf.AgregarDato(k, v)
        if k.upper() == 'CUIT':
            fepdf.CUIT = v  # CUIT del emisor para código de barras

    fepdf.CrearPlantilla(papel=conf_fact.get("papel", "legal"), 
                         orientacion=conf_fact.get("orientacion", "portrait"))
    fepdf.ProcesarPlantilla(num_copias=int(conf_fact.get("copias", 1)),
                            lineas_max=int(conf_fact.get("lineas_max", 24)),
                            qty_pos=conf_fact.get("cant_pos") or 'izq')

    salida = "/tmp/factura.pdf"
    fepdf.GenerarPDF(archivo=salida)
    ##fepdf.MostrarPDF(archivo=salida,imprimir=False)
    
    response.headers['Content-Type'] = "application/pdf"
    return open(salida, "rb")
