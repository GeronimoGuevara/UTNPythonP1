"""
Dada la siguiente tupla:
numeros = (1, 2, 2, 3, 4, 4, 4, 5)
a) Cuenta cuántas veces aparece el número 4 en la tupla.
b) Imprime el resultado.
"""
numeros = (1, 2, 2, 3, 4, 4, 4, 5)
cant4 = 0

for i in numeros:
    if i == 4:
        cant4 = cant4 + 1

print(f"el numero 4 se repite: {cant4} veces.")