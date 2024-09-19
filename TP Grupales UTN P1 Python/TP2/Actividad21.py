#21- Codifique un programa que solicite un número entero mayor a cero y que
#mediante recursión sume todos los números números naturales desde el número
#ingresado hasta 1.
#Ejemplo: Ingreso 10

num = input("ingrese un numero mayor a 0")
num = int(num)
suma = 0


def recursiva(num):

    if num > 0:
        global suma
        suma = suma + num
        recursiva(num-1)
    if num == 0:
        print(suma)

recursiva(num)