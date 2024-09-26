"""
Ejercicio 4: Contar Elementos Pares e Impares
Escribe un programa que pida al usuario una lista de números 
y cuente cuántos de ellos son pares y cuántos son impares.
"""
numeros = input("Ingresa una lista de números separados por espacio: ")
lista_numeros = list(map(int, numeros.split()))
cantpares = 0
cantimpares = 0
for i in lista_numeros:
    if i % 2 == 0:
        cantpares = cantpares + 1
    else:
        cantimpares = cantimpares + 1
    
print("la cantidad de numeros pares es de: ",cantpares, " y la cantidad de numeros impares es de: ",cantimpares)
