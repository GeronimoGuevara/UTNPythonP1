def PedirGolosina(listaCaramelosPedidos, listaCaramelos):
    codigo = int(input("Ingrese el codigo de la golosina a pedir: "))
    
    if codigo in listaCaramelos and listaCaramelos[codigo]["Stock"] > 0:
        print(f"El stock de {listaCaramelos[codigo]['Nombre']} es de {listaCaramelos[codigo]['Stock']} unidades.")
        cantAPedir = int(input("Ingrese la cantidad que desea extraer: "))
        
        if 0 < cantAPedir <= listaCaramelos[codigo]["Stock"]:
            print(f"Usted extrajo {cantAPedir} golosinas.")
            listaCaramelosPedidos[codigo]["CantPedida"] += cantAPedir
            listaCaramelos[codigo]["Stock"] -= cantAPedir
        else:
            print("Cantidad inválida. Verifique el stock disponible.")
    else:
        print("Código inválido o no hay stock de esa golosina.")

    return listaCaramelosPedidos, listaCaramelos

def Rellenar(listaCaramelos, claveTecnico):
    if all(input(f"Ingrese la clave {i+1} del técnico: ") == clave for i, clave in enumerate(claveTecnico)):
        codigo = int(input("Ingrese el código del caramelo a rellenar: "))
        
        if codigo in listaCaramelos:
            cantArellenar = int(input("Ingrese la cantidad a rellenar: "))
            
            while cantArellenar <= 0:
                cantArellenar = int(input("Ingrese una cantidad mayor a 0: "))
                
            listaCaramelos[codigo]["Stock"] += cantArellenar
            print(f"Se ha rellenado {cantArellenar} unidades de {listaCaramelos[codigo]['Nombre']}.")
        else:
            print("Código de golosina no válido.")
    else:
        print("Claves incorrectas. No tiene permiso para ejecutar la recarga.")

    return listaCaramelos

def FinalizarPrograma(listaCaramelosPedidos):
    cantTotalPedidos = sum(item["CantPedida"] for item in listaCaramelosPedidos.values())
    print(f"La cantidad total de golosinas pedidas es de: {cantTotalPedidos}")

def Main():
    listaCaramelos = {
        1 : {"Nombre" : "KitKat", "Stock" : 20},
        2 : {"Nombre" :"Chicles", "Stock" :50},
        3 : {"Nombre" :"Caramelos de Menta", "Stock" : 50},
        4 : {"Nombre" :"Huevo Kinder", "Stock" : 10},
        5 : {"Nombre" :"Cheetos", "Stock" : 10},
        6 : {"Nombre" :"Twix", "Stock" : 10},
        7 : {"Nombre" :"M&Ms", "Stock" : 10},
        8 : {"Nombre" :"Papas Lays", "Stock" : 2},
        9 : {"Nombre" :"Milkybar", "Stock" : 10},
        10 : {"Nombre" :"Alfajor Tofi", "Stock" : 15},
        11 : {"Nombre" :"Lata Coca", "Stock" : 20},
        12 : {"Nombre" :"Chitos", "Stock" : 10}
    }

    diccionarioEmpleados = {
        "1100" : "José Alonso",
        "1200" : "Federico Pacheco",
        "1300" : "Nelson Pereira",
        "1400" : "Osvaldo Tejada",
        "1500" : "Gastón García"
    }

    claveTecnico = ("admin", "CCCDDD", "2020")

    listaCaramelosPedidos = {
        codigo: {"Nombre": golosina["Nombre"], "CantPedida": 0} for codigo, golosina in listaCaramelos.items()
    }

    while True:
        print("\n MENÚ:")
        print("1. Pedir Golosina")
        print("2. Mostrar Menu")
        print("3. Rellenar Caramelos")
        print("4. Apagar Máquina")

        opcion = int(input("Elija una de las opciones: "))
        
        if opcion == 1:
            legajo = input("Ingrese su número de legajo de empleado: ")
            if legajo in diccionarioEmpleados:
                print(f"Empleado autorizado: {diccionarioEmpleados[legajo]}.")
                listaCaramelosPedidos, listaCaramelos = PedirGolosina(listaCaramelosPedidos, listaCaramelos)
            else:
                print("Usted no es un empleado autorizado.")
        
        elif opcion == 2:
            print("Lista de caramelos disponibles:")
            for codigo, golosina in listaCaramelos.items():
                print(f"{codigo}: {golosina['Nombre']} - Stock: {golosina['Stock']}")

        elif opcion == 3:
            listaCaramelos = Rellenar(listaCaramelos, claveTecnico)

        elif opcion == 4:
            FinalizarPrograma(listaCaramelosPedidos)
            print("Finalizando Programa")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    Main()