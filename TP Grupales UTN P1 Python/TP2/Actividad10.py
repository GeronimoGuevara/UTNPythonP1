"""
10- Convertir una cadena a mayúsculas o minúsculas, daremos opción a que el usuario
pida que se desea hacer (convertir a mayúsculas o convertir a minúsculas) y mostrar el
resultado por pantalla. 
"""

cadena =  "hola Como EStas CAPo"

def convertir(opcion):
    if opcion == "1":
        print(cadena.upper())
    elif opcion == "2":
        print(cadena.lower())
    else:
        print("la opcion ingresada no es valida")

print("quiere convertir la cadena en mayusculas(1) o minusculas (2)?")
print("opcion 1")
print("opcion 2")
opcion = input()
convertir(opcion)