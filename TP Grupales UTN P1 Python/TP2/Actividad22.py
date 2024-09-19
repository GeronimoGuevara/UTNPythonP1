"""22- Suma los dígitos de un número ingresado por el usuario de forma recursiva.
Ejemplo: el usuario ingresa 1596
El programa debe sumar 1 + 5 + 9 + 6 """


num = input("Ingrese un nro de 4 digitos")
longitud = len(num)
resultado = 0

print(longitud, num)

def recursiva(longitud, num):
    global resultado
    if longitud > 0:
        resultado = resultado + int(num[longitud-1])
        recursiva(longitud -1,num )
    if longitud == 0:
        print(resultado)

recursiva(longitud, num)