def mostrar_inventario(inventario):
    for codigo,tupla in inventario.items():
        print(f"{codigo},{tupla}")

def buscar_producto(inventario):
    producto = input("ingrese el codigo del producto a buscar, del A001 al A006")
    producto = producto.upper()

    if producto in inventario:
        print(f"el producto es: {inventario[producto]}")
    else:
        print("el producto ingresado no existe")
    
def modificar_precio(inventario):
    producto = input("ingrese el codigo del producto a modificar su precio")
    producto = producto.upper()
    if producto in inventario:
        inventario[producto] = (input("ingrese el nuevo nombre del producto"),input("ingrese el nuevo precio del producto"))
    else:
        print("el producto ingresado no existe")

    print(inventario[producto])

def eliminar_producto(inventario):
    producto = input("Ingrese el codigo del producto que desea eliminar del inventario: ")
    producto = producto.upper()
    if producto in inventario:
        inventario.pop(producto)
    else:
        print("el producto ingresado no existe")

"""
o productos_por_rango_de_precio(inventario, min_precio, max_precio):
Muestra todos los productos cuyo precio esté entre min_precio y
max_precio"""
def productos_por_rango_de_precio(inventario):
    min_precio = int(input("Ingrese el precio mínimo del producto a buscar: "))
    max_precio = int(input("Ingrese el precio máximo del producto a buscar: "))

    if min_precio < max_precio:
        print(f"Productos con precio entre {min_precio} y {max_precio}:")
        for codigo, (nombre, precio) in inventario.items():
            if min_precio <= precio <= max_precio:
                print(f"Código: {codigo}, Producto: {nombre}, Precio: {precio}")
    else:
        print("El precio mínimo debe ser menor que el precio máximo.")

inventario = {
    "A001" : ("monitor",32000),
    "A002" : ("celular",140000),
    "A003" : ("PC Escritorio", 300000),
    "A004" : ("mouse", 15000),
    "A005" : ("teclado", 34000),
    "A006" : ("auriculares", 28000)
}

while True:

    print(" MENÚ:")
    print("1. Mostrar Inventario")
    print("2. Buscar Producto")
    print("3. Modificar Precio")
    print("4. Eliminar Producto")
    print("5. Productos por rango de precio")
    print("6. Finalizar programa")

    opcion = int(input("elija una de las opciones"))
    if opcion == 1:
        mostrar_inventario(inventario)
    elif opcion == 2:
        buscar_producto(inventario)
    elif opcion == 3:
        modificar_precio(inventario)
    elif opcion == 4:
        eliminar_producto(inventario)
    elif opcion == 5:
        productos_por_rango_de_precio(inventario)
    elif opcion == 6:
        print("Finalizando Programa")
        break
    else:
        print(f"usted ingresó la opción: {opcion} y no es valida.")
