#Ejercicio 4: Matriz Transpuesta
#Escribe un programa que calcule la transpuesta de una matriz. La transpuesta de una
#matriz intercambia sus filas por columnas.

import random

def crear_matriz(filas, columnas):
    
    numero = random.randint(1,20)
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


print("Matriz transpuesta:")
transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

for filas in transpuesta:
    print(filas)
