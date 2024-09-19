"""Crea un programa donde se pida el ingreso de una cadena y por medio de
recursión mostrar la cadena de forma inversa.
Ejemplo: Ingreso “computadora de escritorio”
Invertir cadena “oirotircse ed arodatupmoc”"""

string = input("ingrese una palabra")
longitud = len(string)

def recursiva(longitud, string):
    if longitud > 0:
        print(string[longitud-1])
        recursiva(longitud -1, string)

recursiva(longitud, string)