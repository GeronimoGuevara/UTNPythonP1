"""Ejercicio 5: Multiplicar Elementos por un Valor
Escribe un programa que multiplique cada elemento de una lista de 
números por un valor ingresado por el usuario."""

numeros = input("Ingresa una lista de números separados por espacio: ")
lista_numeros = list(map(int, numeros.split()))
mult = int(input("ingrese el multiplicador de la lista"))
resultado = 0

lista_numeros = [x*mult for x in lista_numeros]
print(lista_numeros)
