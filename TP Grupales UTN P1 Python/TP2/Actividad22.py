# 22- Suma los dígitos de un número ingresado por el usuario de forma recursiva.
# Ejemplo: el usuario ingresa 1596
# El programa debe sumar 1 + 5 + 9 + 6 
num = input("ingrese un numero para calcular sus digitos")
longitud = len(num)
resultado = 0

def recursividad(longitud,num):
    global resultado
    if longitud > 0:
        resultado = resultado + int(num[longitud-1])
        recursividad(longitud-1,num)
    if longitud == 0:
        print(resultado)

recursividad(num)