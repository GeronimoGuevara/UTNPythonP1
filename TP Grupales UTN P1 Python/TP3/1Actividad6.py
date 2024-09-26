"""Ejercicio 6: Eliminar Duplicados
Escribe un programa que permita al usuario ingresar una lista 
de números y elimine los elementos duplicados.
Pista:
 Utiliza la función set().
"""

nros = input("Ingrese los nros")
array = list(map(int,nros.split()))
x = set(array)
print(x)
