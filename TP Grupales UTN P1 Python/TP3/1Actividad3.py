"""Ejercicio 3: Invertir una Lista
Escribe un programa que permita al usuario ingresar 
una lista y la invierta"""

numeros = input("Ingresa una lista de números separados por espacio: ")
lista_numeros = list(map(int, numeros.split()))
lista_numeros.reverse()
print((lista_numeros))