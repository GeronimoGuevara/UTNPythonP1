""""
7- Solicite el ingreso de una cadena y determine el tamaño de la misma y cuantas
vocales tiene en total.
"""

cantidad = 0
vocales = ["a","e","i","o","u"]
cadena = input("Ingrese una cadena de texto")
largo = len(cadena)


"""for ["a","e","i","o","u"] in cadena:
    vocales = vocales + 1
""" 


for i in range(1,largo,1):
    if cadena[i] in vocales :
        cantidad = cantidad + 1

print(cantidad) 