#Ejercicio 2: Suma de Todos los Elementos
#Escribe un programa que calcule la suma de todos los elementos en una lista bidimensional.
#Pista: Aplique la función sum

def sumar_valores(matriz):
    
    suma = sum(sum(fila) for fila in matriz)
    
    return suma
    
def crear_matriz(filas, columnas):
    
    i = 1 
    matriz = []  
    
    for _ in range(filas): 
    
        fila = []  
        
        for _ in range(columnas):
            
            fila.append(i)  
            
            i += 1  
            
        matriz.append(fila)  
    
    return matriz

filas = 3
columnas = 3

matriz = crear_matriz(filas,columnas)
print("La matriz es")
for filas in matriz:
    print(filas)

suma = sumar_valores(matriz)
print(f"La suma de todos los numeros es {suma}")
