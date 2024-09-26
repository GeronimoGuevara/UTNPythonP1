"""Ejercicio 8: Encontrar Elementos Repetidos
Escribe un programa que identifique y muestre los elementos que se 
repiten en una lista.
Pista:
Utiliza un diccionario o un conjunto (set) para hacer el seguimiento 
de los elementos.
"""

def encontrar_elementos_repetidos(lista):
    vistos = set()
    repetidos = set()

    for elemento in lista:
        if elemento in vistos:
            repetidos.add(elemento)
        else:
            vistos.add(elemento)

    return list(repetidos)

numeros = input("Ingresa una lista de números separados por espacio: ")
lista_numeros = list(map(int, numeros.split()))
repetidos = encontrar_elementos_repetidos(lista_numeros)
print("Elementos repetidos:", repetidos)
