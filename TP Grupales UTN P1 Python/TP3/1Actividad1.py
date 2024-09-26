"""
Ejercicio 1: Suma de Elementos
Escribe un programa que permita al usuario ingresar 
una lista de números y calcule la suma de todos 
los elementos en la lista.
"""

numeros = input("Ingresa una lista de números separados por espacio: ")
lista_numeros = list(map(int, numeros.split()))
suma = sum(lista_numeros)
print(f"La suma de los números es: {suma}")
