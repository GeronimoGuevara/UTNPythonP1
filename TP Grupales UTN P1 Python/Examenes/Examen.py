import random
def GenerarManual(cantColumnas,cantFilas):
    print("Elegiste la opcion 1 Manual")
    matriz = [[0]* cantColumnas for i in range(cantFilas)]
    for i in range(cantFilas):
        for j in range(cantColumnas):
            valor = int(input(f"Ingrese un valor para su matriz entre el 0 y el 999 para la posicion |{i}{j}|."))
            while valor >999 or valor < 0:
                valor = int(input(f"Ingrese un valor para su matriz entre el 0 y el 999 para la posicion |{i}{j}|."))
            matriz[i][j]= valor
    return matriz

def GenerarAleatorio(cantColumnas,cantiFilas):
    print("elegiste la opcion 2 Aleatoria")
    matriz = [[0]*cantColumnas for i in range(cantiFilas)]
    for i in range(cantiFilas):
        for j in range(cantColumnas):
            valor = random.randint(0,999)
            matriz[i][j] = valor
    return matriz

def SumarFilas(matriz):
    sumar_fila = [0] * len(matriz)
    for i in range(len(matriz)):
        sumarvaloresfila = 0
        for j in matriz[i]:
            sumarvaloresfila += j
        sumar_fila[i]=sumarvaloresfila
    
    for i in range(len(sumar_fila)):
        print(f"La suma de la fila [{i}] = {sumar_fila[i]}")
    return sumar_fila

def OrdenarMayorAMenor(sumaDeFilas__):#metodo burbuja
    lista_tuplas = [(sumaDeFilas__[i],i) for i in range(len(sumaDeFilas__))]
    n = len(lista_tuplas)
    for i in range(n):
        for j in range(0,n-i-1):
            if lista_tuplas[j][0] < lista_tuplas[j+1][0]:
                lista_tuplas[j], lista_tuplas[j+1] = lista_tuplas[j+1],lista_tuplas[j]
        print("La Lista ordenada de mayor a menor con su orden original a la derecha es: ")
        for j in lista_tuplas:
            print(j)
        return lista_tuplas

def SumaFinalTotal(sumaDeFilas__):
    sumaTotal = 0
    for i in range(len(sumaDeFilas__)):
        sumaTotal = sumaTotal + sumaDeFilas__[i]
    print(f"la suma total de las filas es de: {sumaTotal}")
    return sumaTotal

def Main():
    cantFilas = int(input("Ingrese la cantidad de filas de su matriz (>=3)"))
    while cantFilas<3:
        cantFilas = int(input("Ingrese la cantidad de filas de su matriz (>=3)"))
    cantColumnas = int(input("Ingrese la cantidad de columnas de su matriz (>=2)"))
    while cantColumnas <2:
        cantColumnas = int(input("Ingrese la cantidad de columnas de su matriz (>=2)"))

    while True:
        opcion = int(input("Ingrese como quiere generar la matriz: \n 1. Manual \n 2. Aleatorio \n Opcion:  "))
        if opcion == 1:
            matriz = GenerarManual(cantColumnas,cantFilas)
            break
        elif opcion == 2:
            matriz = GenerarAleatorio(cantColumnas,cantFilas)
            break
    print("La matriz generada es:")
    for i in matriz:
        print(i)
    sumaDeFilas__ = SumarFilas(matriz)
    OrdenarMayorAMenor(sumaDeFilas__)
    SumaFinalTotal(sumaDeFilas__)


if __name__ == "__main__":
    Main()