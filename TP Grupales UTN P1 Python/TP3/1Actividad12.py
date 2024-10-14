"""Ejercicio 12: Sumar Listas Elemento por Elemento
Escribe un programa que sume dos listas de números elemento por elemento. Las
listas deben tener la misma longitud.
"""
import numpy as np # type: ignore
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
suma = array1 + array2
print("Suma de arrays:", suma)
