"""
Ejercicio 2: Encontrar el Mayor y el Menor
Escribe un programa que pida al usuario una lista de
números y encuentre el mayor y el menor de ellos.
"""
numeros = input("Ingresa una lista de números separados por espacio: ")
lista_numeros = list(map(int, numeros.split()))
minimo = print("el numero mas chico es: ",min(lista_numeros))
maximo = print("el numero mas grande es: ",max(lista_numeros))
