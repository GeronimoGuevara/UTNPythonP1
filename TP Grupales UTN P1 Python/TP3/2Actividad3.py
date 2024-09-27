#Ejercicio 3: Suma de Cada Fila
#Modifica el programa anterior para que imprima la suma de cada fila de la lista bidimensional.

    
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

for i, filas in enumerate(matriz):
    
    suma = sum(filas)
    print(f"Los elementos de la fila {i+1} suman {suma}")
