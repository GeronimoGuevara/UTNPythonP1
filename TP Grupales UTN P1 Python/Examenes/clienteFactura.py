# calculoFactura.py

# Atributos Globales de la Factura
fechaFactura = ""
numeroFactura = 0
letraFactura = ""
totalFactura = 0.0
montoIva = 0.0
clienteFactura = ""
detallesFactura = []

# Lista de Artículos
articulos = [
    [101, "Leche", 250],
    [102, "Gaseosa", 300],
    [103, "Fideos", 150],
    [104, "Arroz", 280],
    [105, "Vino", 1200],
    [106, "Manteca", 200],
    [107, "Lavandina", 180],
    [108, "Detergente", 460],
    [109, "Jabón en Polvo", 960],
    [110, "Galletas", 600]
]

# Diccionario de Clientes
clientes = {
    "20110425417": "Rodolfo Fernandez",
    "30527419655": "Los Pollos Hnos",
    "27289425478": "Andrea Pereira",
    "33536549878": "Multimarca Repuestos",
    "20291122568": "Luis Peric"
}

# Funciones necesarias
def solicitar_datos_factura():
    global fechaFactura, numeroFactura
    fechaFactura = input("Ingrese la fecha de la factura: ")
    numeroFactura = int(input("Ingrese el número de la factura: "))

def obtener_cliente():
    global clienteFactura
    cuit = input("Ingrese el CUIT del cliente: ")
    if cuit.startswith(("20", "27", "30", "33")) and cuit in clientes:
        clienteFactura = clientes[cuit]
    else:
        clienteFactura = "Consumidor Final"
    return cuit

def agregar_articulo():
    global detallesFactura
    while True:
        codigo = int(input("Ingrese el código del artículo (0000 para finalizar): "))
        if codigo == 0:
            break
        articulo = next((a for a in articulos if a[0] == codigo), None)
        if articulo:
            cantidad = int(input(f"Ingrese la cantidad de {articulo[1]}: "))
            subtotal = cantidad * articulo[2]
            detallesFactura.append([articulo[0], articulo[1], cantidad, articulo[2], subtotal])
        else:
            print("Código Incorrecto")

def calcular_total():
    return sum([detalle[4] for detalle in detallesFactura])

def calcular_iva(cuit):
    global montoIva
    total = calcular_total()
    if cuit.startswith(("30", "33")):
        montoIva = total * 0.21
    else:
        montoIva = 0.0

def asignar_letra(cuit):
    global letraFactura
    if cuit.startswith(("30", "33")):
        letraFactura = "A"
    else:
        letraFactura = "B"

def calcular_total_factura():
    global totalFactura
    subtotal = calcular_total()
    if letraFactura == "B":
        totalFactura = subtotal + montoIva
    else:
        totalFactura = subtotal

def imprimir_factura():
    print(f"Fecha: {fechaFactura}")
    print(f"Número: {numeroFactura}")
    print(f"Letra: {letraFactura}")
    print(f"Cliente: {clienteFactura}")
    print("\nCódigo Artículo | Nombre | Cantidad | Precio Unitario | Subtotal")
    for detalle in detallesFactura:
        print(f"{detalle[0]:<17} {detalle[1]:<8} {detalle[2]:<10} {detalle[3]:<17} {detalle[4]:<8}")
    print(f"\nIVA: {montoIva}")
    print(f"Total: {totalFactura}")

# Ejecución del programa
solicitar_datos_factura()
cuit = obtener_cliente()
agregar_articulo()
calcular_iva(cuit)
asignar_letra(cuit)
calcular_total_factura()
imprimir_factura()
