def PedirGolosina(listaCaramelosPedidos,listaCaramelos):
    codigo = 0
    cantAPedir = 0
    codigo = int(input("Ingrese el codigo de la golosina a pedir:"))
    if codigo in listaCaramelos and listaCaramelos[codigo]["Stock"] != 0:
        print("El stock de esa golosina es de: ")
        print(listaCaramelos[codigo])
        cantAPedir = int(input("Ingrese la cantidad que desea extraer: "))
        if cantAPedir <= listaCaramelos[codigo]["Stock"] and cantAPedir > 0:
            print(f"Usted extrajo {cantAPedir} golosinas")
            listaCaramelosPedidos[codigo]["CantPedida"] = listaCaramelosPedidos[codigo]["CantPedida"] + cantAPedir
            listaCaramelos[codigo]["Stock"] = listaCaramelos[codigo]["Stock"] - listaCaramelosPedidos[codigo]["CantPedida"]
    else:
        print("no hay stock de esa golosina")

    return listaCaramelosPedidos,listaCaramelos

def Rellenar(listaCaramelos,claveTecnico):
    paso11 = input("Ingrese la calve 1 del tecnico: ")
    if paso11 == claveTecnico[0]:
        paso22 = input("Ingrese la clave 2 del tecnico ")
        if paso22 == claveTecnico[1]:
            paso33 = input("Ingrese la clave 3 del tecnico")
            if paso33 == claveTecnico[2]:
                codigo = input("Ingrese el codigo del caramelo a rellenar: ")
                if codigo in listaCaramelos:
                    cantArellenar = int(input("Ingrese la cantidad a rellenar: "))
                    while cantArellenar < 0:
                        cantArellenar = int(input("Ingrese una cantidad a rellenar mayor a 0: "))
                    listaCaramelos[codigo]["Stock"] = listaCaramelos[codigo]["Stock"] + cantArellenar
            else:
                print("Usted no tiene permiso para ejecutar la recarga.")
        else:
            print("Usted no tiene permiso para ejecutar la recarga.")
    else:
        print("Usted no tiene permiso para ejecutar la recarga.")
    return listaCaramelos

def FinalizarPrograma(listaCaramelosPedidos):
    cantTotalPedidos = 0
    for codigo in listaCaramelosPedidos:
        cantTotalPedidos = cantTotalPedidos + listaCaramelosPedidos[codigo]["CantPedida"]
                    
def Main():

    listaCaramelos = {
        1 : {"Nombre" : "KitKa", "Stock" : 20},
        2 : {"Nombre" :"Chicles", "Stock" :50},
        3 : {"Nombre" :"Caramelos de Menta","Stock" : 50},
        4 : {"Nombre" :"Huevo Kinder","Stock" : 10},
        5 : {"Nombre" :"Chetoos","Stock" : 10},
        6 : {"Nombre" :"Twix" ,"Stock" :10},
        7 : {"Nombre" :"M&MS","Stock" : 10},
        8 : {"Nombre" :"Papas Lays","Stock" : 2},
        9 : {"Nombre" :"Milkybar","Stock" : 10},
        10 : {"Nombre" :"Alfajor Tofi ","Stock" :15},
        11 : {"Nombre" :"Lata Coca", "Stock" :20},
        12 : {"Nombre" :"Chitos ","Stock" :10}
    }

    diccionarioEmpleados = {
        "1100" : "José Alonso",
        "1200" : "Federico Pacheco",
        "1300" : "Nelson Pereira",
        "1400" : "Osvaldo Tejada",
        "1500" : "Gastón Garcia"
    }

    claveTecnico = ("admin","CCCDDD","2020")

    listaCaramelosPedidos = {
        1 : {"Nombre" : "KitKa", "CantPedida" : 0},
        2 : {"Nombre" :"Chicles", "CantPedida" :0},
        3 : {"Nombre" :"Caramelos de Menta","CantPedida" : 0},
        4 : {"Nombre" :"Huevo Kinder","CantPedida" : 0},
        5 : {"Nombre" :"Chetoos","CantPedida" : 0},
        6 : {"Nombre" :"Twix" ,"CantPedida" :0},
        7 : {"Nombre" :"M&MS","CantPedida" : 0},
        8 : {"Nombre" :"Papas Lays","CantPedida" : 0},
        9 : {"Nombre" :"Milkybar","CantPedida" : 0},
        10 : {"Nombre" :"Alfajor Tofi ","CantPedida" :0},
        11 : {"Nombre" :"Lata Coca", "CantPedida" :0},
        12 : {"Nombre" :"Chitos ","CantPedida" :0}
    }
    while True:

        print(" MENÚ:")
        print("1. Pedir Golosina")
        print("2. Mostrar Menu")
        print("3. Rellenar Caramelos")
        print("4. Apagar Maquina ")
        cantTotalPedida = 0
        opcion = int(input("elija una de las opciones"))
        if opcion == 1:
            legajo = input("Ingrese su numero de legajo de empleado: ")
            if legajo in diccionarioEmpleados:
                print("Usted es empleado puede retirar golosinas")
                listaCaramelosPedidos = PedirGolosina(listaCaramelosPedidos,listaCaramelos)
            else:
                print("Usted NO es un empleado")

        elif opcion == 2:
            print("Lista caramelos Disponibles.")
            for i,lista in listaCaramelos.items():
                print(i,lista)
        elif opcion == 3:
            Rellenar(listaCaramelos,claveTecnico)
        elif opcion == 4:
            print(f"La cantidad total de golosinas pedidas es de: {cantTotalPedida}")
            print("Finalizando Programa")
            break
        else:
            print(f"usted ingresó la opción: {opcion} y no es valida.")


if __name__ == "__main__":
    Main()