"""Ejercicio 13: Explique y ejemplifique la librería NumPy para trabajar con matrices y
arrays"""
# primero que nada numpy es una libreria propia de python que se utiliza para trabajar con matrices
# y arrays grandes y se puede utilizar por ejemplo para la creacion de un array, la suma de dos arrays
# por ejemplo:
import numpy as np
array1 = np.array([1,2,3,4,5])
array2 = np.array([5,4,3,2,1])
print(array1) 
print(array2)
producto = array1 * array2
print(producto)