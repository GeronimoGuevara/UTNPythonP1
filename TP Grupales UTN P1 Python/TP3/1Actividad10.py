"""Ejercicio 10: Eliminar un Elemento por su Índice
Escribe un programa que permita al usuario ingresar una lista de números y eliminar
un elemento en un índice especificado."""

numero = input("ingrese una lista separando por espacios")
lista = list(map(int,numero.split()))
elemento_eliminado = 0
elim = int(input("ingrese la pocision del numero que quiere eliminar"))
if elim <= len(lista):
    elemento_eliminado = lista.pop(elim-1)

    print(lista)
    print(elemento_eliminado)

else:
    print("el indice proporcionado esta fuera de rango")