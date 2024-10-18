import random
def GenerarManual(cantFilas,cantColumnas):
    matriz = [[0] * cantColumnas for i in range(cantFilas)]

    for i in range(cantFilas):
        for j in range(cantColumnas):
            valor = int(input(f"Ingrese un numero para la posicion {i}{j} "))
            while valor > 999 or valor < 0:
                valor = int(input(f"Ingrese un numero entre 0 y 999 para la posicion {i}{j} "))
            matriz[i][j] = valor
    return matriz

def GenerarAleatorio(cantFilas,cantColumnas):
    matriz = [[0] * cantColumnas for i in range(cantFilas)]
    
    for i in range(cantFilas):
        for j in range(cantColumnas):
            matriz[i][j] = random.randint(0,999)
    return matriz

def SumarFilas(matriz):
    sumar_filas = [0] * len(matriz)
    for i in range(len(matriz)):
        sumarValores = 0
        for j in matriz[i]:
            sumarValores += j
        sumar_filas[i] = sumarValores
    
    for i in range(len(sumar_filas)):
        print(f"la suma de la fila [{i}] = {sumar_filas[i]}")
    return sumar_filas

def Main():
    cantFilas = int(input("Ingrese la cantidad de filas de la matriz >=3 "))
    while cantFilas<3:
        cantFilas = int(input("Ingrese la cantidad de filas de la matriz >=3 "))
    cantColumnas = int(input("Ingrese la cantidad de columnas de la matriz >= 2 "))
    while cantColumnas<2:
        cantColumnas = int(input("Ingrese la cantidad de columnas de la matriz >= 2 "))

    while True:
        opcion = int(input("Como quiere generar la matriz: \n 1. Manual \n 2. Aleatoria \n Opcion : "))
        if opcion == 1:
            matriz = GenerarManual(cantFilas,cantColumnas)
            break
        elif opcion == 2:
            matriz = GenerarAleatorio(cantFilas,cantColumnas)
            break
        else:
            print("Ingrese una opcion valida")
    
    for i in matriz:
        print(i)

    sumarDeLasFilas = SumarFilas(matriz)
    


if __name__ == "__main__":
    Main()