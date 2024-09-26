"""Ejercicio 7: Promedio de una Lista
Escribe un programa que permita al usuario ingresar una lista de 
números y calcule el promedio de los elementos."""

numeros = input("Ingresa una lista de números separados por espacio: ")
lista_numeros = list(map(int, numeros.split()))
suma = 0

for i in range(len(lista_numeros)):
    suma = suma + lista_numeros[i]

promedio = suma / len(lista_numeros)
print(promedio)