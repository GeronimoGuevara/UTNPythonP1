#Ejercicio 9: Matriz Identidad Inversa
#Crea un programa que genere una matriz identidad inversa de tamaño n.

tamanio = int(input("Ingrese el tamaño de la matriz identidad inversa: "))

matriz_identidad = [[1 if i == j else 0 for j in range(tamanio-1, -1, -1)] for i in range(tamanio)]

# ? No entiendo por qué funciona con el i == j si se supone que nunca serían iguales

for filas in matriz_identidad:
    print(filas)
