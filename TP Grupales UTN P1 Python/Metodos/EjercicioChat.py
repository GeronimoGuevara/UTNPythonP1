import random

def GenerarManual(cantColumnas,cantFilas):
    matriz = [[0] * cantColumnas for i in range(cantFilas)]
    for i in range(cantFilas):
        for j in range(cantColumnas):
            valor = int(input(f"Ingrese el valor de la posicion {i}{j}"))
            while valor > 999 or valor < 0:
                valor = int(input(f"Ingrese el valor de la posicion {i}{j}"))
            matriz[i][j] = valor
    return matriz

def GenerarAleatorio(cantColumnas,cantFilas):
    matriz = [[0] * cantColumnas for i in range(cantFilas)]
    for i in range(cantFilas):
        for j in range(cantColumnas):
            valor = random.randint(0,999)
            matriz[i][j] = valor
    return matriz
    
def SumarColumnas(matriz):

    listaSumada = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == 0:
                listaSumada.append(matriz[i][j])
            else:
                listaSumada[j] += matriz[i][j]
    return listaSumada

def OrdenarSumas(listaSumada):
    lista_Tuplas = [(listaSumada[i],i)for i in range(len(listaSumada))]
    n = len(lista_Tuplas)
    for i in range(n):
        for j in range(0,n-i-1):
            if lista_Tuplas[j][0] < lista_Tuplas[j+1][0]:
                lista_Tuplas[j],lista_Tuplas[j+1] = lista_Tuplas[j+1] , lista_Tuplas[j]
        print("la lista sumada de mayor a menor con su orden es")
        for j in lista_Tuplas:
            print(j)
        return lista_Tuplas
    
def Promedio(matriz):
    contador=0
    suma=0
    columnas=len(matriz[0])
    filas=len(matriz)
    if columnas>0 and filas>0:
        for i in range(filas):
            for j in range(columnas):
            
                contador+=1
                suma=suma+matriz[i][j]  
     
    if contador>0:    
        promedio=suma/contador    
        print(f"El promedio es", promedio)
    
def eliminarDeLaLista(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])-1,-1,-1):
            if j % 2 == 0 :
                lista[i].pop(j)
    return lista

def Main():
    cantFilas = int(input("Ingrese la cantidad de filas de su matriz >= 3. "))
    while cantFilas < 3:
        cantFilas = int(input("Ingrese la cantidad de filas de su matriz >= 3. "))
    cantColumnas = int(input("Ingrese la cantidad de columnas de su matriz >= 2. "))
    while cantColumnas < 2:
        cantColumnas = int(input("Ingrese la cantidad de columnas de su matriz >= 2. "))
    
    while True:
        opcion = int(input("Ingrese la opcion del menu: \n 1. Manual \n 2. Aleatorio \n Opcion: "))
        if opcion == 1:
            matriz = GenerarManual(cantColumnas,cantFilas)
            break
        elif opcion == 2:
            matriz = GenerarAleatorio(cantColumnas,cantFilas)
            break
        else:
            print("Igrese una opcion valida")
    
    for i in matriz:
        print(i)
    
    print("La suma de las columnas de la lista es: ")
    print(SumarColumnas(matriz))

    
    listaSumada = SumarColumnas(matriz)
    listaOrdenada = OrdenarSumas(listaSumada)
    Promedio(matriz)
    nuevaMatriz = eliminarDeLaLista(matriz)
    print(nuevaMatriz)

if __name__ == "__main__":
    Main()