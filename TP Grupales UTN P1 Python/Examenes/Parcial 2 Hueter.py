def mostrarFactura(detalleFactura,fechaFactura,numeroFactura,clienteFactura,montoIva,letraFactura,totalFactura):
    
    # Imprimir la factura con el formato
    print(f"\nFECHA: {fechaFactura}")
    print(f"NUMERO: {numeroFactura}")
    print(f"LETRA: {letraFactura}")
    print(f"CLIENTE: {clienteFactura}")
    print(f"{'Código articulo':<16} {'Nombre artículo':<16} {'Cantidad':<9} {'Precio unitario':<16}{'Subtotal':<8}")

    for detalle in detalleFactura:
        codigo, nombre, cantidad, precio_unitario, subtotal = detalle
        print(f"{codigo:<16} {nombre:<16} {cantidad:<9} {precio_unitario:<16} {subtotal:<8}")

    print(f"\n{'IVA:':>60} {montoIva:>5}")
    print(f"{'Total:':>60} {totalFactura:>5}")
   
def asignarValorIvayLetraFactura(cuit,clienteFactura,totalFactura):
    
    montoIva = 0
    letraFactura = ""
    totalFactura = totalFactura
    
    if str(cuit).startswith("20") or str(cuit).startswith("27") or str(clienteFactura) == "Consumidor Final":
        
        montoIva = 0
        letraFactura = "B"
        totalFactura += montoIva
        
    elif str(cuit).startswith("30") or str(cuit).startswith("33"):
        
        montoIva = totalFactura * 0.21
        letraFactura = "A"
        totalFactura = totalFactura
        
    return montoIva,letraFactura,totalFactura

def calcularTotal(detalleFactura):
    
    sumaSubtotal = 0
    
    for detalle in detalleFactura:
        
        sumaSubtotal += detalle[4]
        
    return sumaSubtotal
    
def cargarArticulos(detalleFactura,articulos,codigoArticulo,cantidadArt):
    
    for articulo in articulos:
        
        codigo = codigoArticulo
        nombre = articulos[codigoArticulo-101][1]
        precio_unitario = articulos[codigoArticulo-101][2]
        subtotal = precio_unitario * cantidadArt
        
    detalleFactura.append([codigo,nombre,cantidadArt,precio_unitario,subtotal])
        
    return detalleFactura
            
def validarCodigo(codigoArticulo,articulos):
    
    for articulo in articulos:
        while articulos[codigoArticulo-101][0] != codigoArticulo:
            codigoArticulo = int(input("Código incorrecto. Intente nuevamente"))
            
        if articulos[codigoArticulo-101][0] == codigoArticulo:
            return True
 
def mostrarArticulos(articulos):
    
    print("\nARTICULOS DISPONIBLES:")
    
    #f"{valor:<ancho}"
    print(f"{'Código artículo':<15} {'Nombre artículo':<20} {'Precio unitario':<15}")

    for articulo in articulos:
        codigo, nombre, precio = articulo
        print(f"{codigo:<15} {nombre:<20} {precio:<15}")
    
def validarCuit(cuit):
    
    if str(cuit).startswith("20") or str(cuit).startswith("27") or str(cuit).startswith("30") or str(cuit).startswith("33"):
        
        if cuit in clientes:
            
            return True
        
        else:
            print("\nNo pertenece a la empresa")
            return False
        
    else:
        print("Por favor, ingrese un numero de CUIT válido.")
        
def solicitarDatosFactura():
    fechaFactura = input("Ingrese la fecha de la factura.\nDD/MM/AAAA\n")
    numeroFactura = int(input("\nIngrese el numero de factura.\n"))
    
    cuit = int(input("\nIngrese el numero de CUIT.\n"))
    if validarCuit(cuit) == True:
        clienteFactura = clientes[cuit]
    else:
        clienteFactura = "Consumidor Final"
    
    mostrarArticulos(articulos)
    codigoArticulo = int(input("\nIngrese el codigo del articulo a facturar.\n"))
    while codigoArticulo < 101 or codigoArticulo > 110:
        codigoArticulo = int(input("\nCodigo de articulo incorrecto. Intente nuevamente.\n"))

    while codigoArticulo != 000:
        if validarCodigo(codigoArticulo,articulos):
            cantidadArt = int(input("\nIngrese la cantidad de ese articulo a facturar.\n"))

            cargarArticulos(detalleFactura,articulos,codigoArticulo,cantidadArt)
            
            codigoArticulo = int(input("\nIngrese el codigo del articulo a facturar. Ingrese 000 para finalizar la carga de artículos\n"))
            
        
    totalFactura = calcularTotal(detalleFactura)
    
    montoIva, letraFactura, totalFactura = asignarValorIvayLetraFactura(cuit,clienteFactura,totalFactura)
    
    mostrarFactura(detalleFactura,fechaFactura,numeroFactura,clienteFactura,montoIva,letraFactura,totalFactura)


detalleFactura = []

articulos = [
    [101, "Leche", 250],
    [102, "Gaseosa", 300],
    [103, "Fideos", 150],
    [104, "Arroz", 280],
    [105, "Vino", 1200],
    [106, "Manteca",200],
    [107, "Lavandina",180],
    [108, "Detergente",460],
    [109, "Jabon en polvo",960],
    [110, "Galletas",600]
    ]

clientes = {
    
    20443096219:"Rodolfo Fernandez",
    30443096219:"Los Pollos Hnos",
    27443096219:"Andrea Pereira",
    33443096219:"Multimarca Repuestos",
    20443096217:"Luis Peric"
}

#Ejecutar
solicitarDatosFactura()
