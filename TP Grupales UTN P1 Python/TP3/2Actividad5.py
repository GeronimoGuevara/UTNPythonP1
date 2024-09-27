#Ejercicio 5: Encontrar el Elemento Mayor
#Escribe un programa que encuentre el valor más grande en una lista bidimensional.

import random

def numero_mayor(matriz):
    
    mayores = []
    
    for filas in matriz:
        
        mayor_fila = max(filas)
        mayores.append(mayor_fila)
        
    mayor = max(mayores)
    
    return mayor
        
    
def crear_matriz(filas, columnas):
    
    numero = random.randint(1,50)
    matriz = []  
    
    for _ in range(filas): 
    
        fila = []  
        
        for _ in range(columnas):
            
            fila.append(numero)  
            
            numero = random.randint(1,20)
            
        matriz.append(fila)  
    
    return matriz

filas = 3
columnas = 3

matriz = crear_matriz(filas,columnas)
print("Matriz original:")
for filas in matriz:
    print(filas)
    
mayor = numero_mayor(matriz)
print(f"El numero mayor de la matriz es: {mayor}")
