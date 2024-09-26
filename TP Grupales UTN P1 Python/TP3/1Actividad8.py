"""Ejercicio 8: Encontrar Elementos Repetidos
Escribe un programa que identifique y muestre los elementos que se 
repiten en una lista.
Pista:
Utiliza un diccionario o un conjunto (set) para hacer el seguimiento 
de los elementos.
"""
numeros = input("Ingresa una lista de números separados por espacio: ")
lista_numeros = list(map(int, numeros.split()))

print(lista_numeros)

vistos = set()
repetidos = set()

for elemento in lista_numeros:
    if elemento in vistos:
        repetidos.add(elemento)
    else:
        vistos.add(elemento)

print(repetidos)