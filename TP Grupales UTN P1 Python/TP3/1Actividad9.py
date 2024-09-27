"""Ejercicio 9: Lista de Números Primos
Escribe un programa que permita al usuario ingresar una lista de números y filtre los
números primos.
Pista:
 Usa una función para verificar si un número es primo."""

def encontrar_numeros_primos(lista):
    primos = set()
    for i in lista:
        if i > 1:
            divisores = 0
            if i == 2:
                primos.add(i)

            else:
                for x in range(2, i):
                    if i % x == 0:
                        divisores += 1
                        break

                if divisores == 0:
                    primos.add(i)

    return primos

num = input("Ingresa una lista de números separados por espacio: ")
lista_numeros = list(map(int, num.split()))

numeros_primos = encontrar_numeros_primos(lista_numeros)
print("Los números primos son:", numeros_primos)
