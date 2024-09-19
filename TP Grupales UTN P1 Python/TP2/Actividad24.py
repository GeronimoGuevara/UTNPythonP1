"""Crea un programa que lea una cadena de texto carácter por carácter usando
recursión.
Ejemplo: Ingreso “UTN FRM Mza”
Salida: U
T
N
F
R
M
M
z
a"""

string = input("ingrese una palabra")
longitud = len(string)
contador = 0

def recursiva(longitud, string):
    global contador
    if longitud > 0:
        recursiva(longitud -1, string)
        contador = contador + 1  
        print(string[contador -1])

recursiva(longitud, string)