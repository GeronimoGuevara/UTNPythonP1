#Ejercicio 8: Matriz Identidad
#Crea un programa que genere una matriz identidad de tamaño n. Una matriz identidad
#es una matriz cuadrada donde los elementos de la diagonal principal son 1 y el resto son 0.

tamanio = int(input("Ingrese el tamaño de la matriz identidad: "))

matriz_identidad = [[1 if i == j else 0 for j in range(tamanio)] for i in range(tamanio)]

for filas in matriz_identidad:
    print(filas)
