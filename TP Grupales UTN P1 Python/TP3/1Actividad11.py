"""Ejercicio 11: Contar Ocurrencias de un Elemento
Escribe un programa que permita al usuario ingresar una lista y un número, y cuente
cuántas veces aparece ese número en la lista.
"""
def contar_ocurrencias(lista, rep):
    ocurrencias = 0 
    for i in lista:
        if i == rep:
            ocurrencias += 1
    return ocurrencias

numero = input("Ingrese una lista de números separados por espacios: ")
lista_numeros = list(map(int, numero.split()))

rep = int(input("¿Qué número desea controlar para ver si se repite? "))

ocurrencias = contar_ocurrencias(lista_numeros, rep)

if ocurrencias == 1:
    print("El número ",rep," se repite una sola vez.")
elif ocurrencias > 1:
    print("El número ",rep," se repite ",ocurrencias, " veces.")
else:
    print("El número ",rep," no se encuentra en la lista.")
