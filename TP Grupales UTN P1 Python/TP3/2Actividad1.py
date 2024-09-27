#Ejercicio 1: Crear una Matriz de Números 
#Crea una función que reciba dos parámetros: el número de filas y columnas. La función
#debe generar una matriz de ese tamaño, donde los valores son números enteros
#consecutivos empezando desde 1.

def crear_matriz(filas, columnas):
    
    i = 1 
    matriz = []  
    
    for _ in range(filas): 
    # _ significa que se esta iterando un número determinado de veces, 
    #pero el valor en sí de la iteración no es importante o no se va a utilizar en el cuerpo del bucle.
        
        fila = []  
        
        for _ in range(columnas):
            
            fila.append(i)  
            
            i += 1  
            
        matriz.append(fila)  
    
    return matriz

filas = int(input("Ingrese el numero de filas "))
columnas = int(input("Ingrese el numero de columnas "))

matriz = crear_matriz(filas,columnas)
    
for filas in matriz:
    print(filas)
