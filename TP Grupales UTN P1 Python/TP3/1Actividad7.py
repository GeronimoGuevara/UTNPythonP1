"""Ejercicio 7: Promedio de una Lista
Escribe un programa que permita al usuario ingresar una lista de 
números y calcule el promedio de los elementos."""
import numpy as np

numeros = input("Ingresa una lista de números separados por espacio: ")
lista_numeros = list(map(int, numeros.split()))

media = np.mean(lista_numeros)
print("Media del array:", media)
