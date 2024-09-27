#Ejercicio 6: Multiplicar una Matriz por un Escalar
#Escribe un programa que multiplique cada elemento de una lista bidimensional por un
#valor escalar dado por el usuario.
    
matriz = [
[1, 2, 3], 
[4, 5, 6],
[7, 8, 9]
]

print("Matriz:")
for fila in matriz:
    
    for elemento in fila:
        
        print(elemento, end=" ")
    
    print()

valor_escalar = int(input("Indique el numero por el cual se multiplicarán los valores de la matriz: "))


print("Matriz con valores multiplicados:")
for fila in matriz:
    
    for elemento in fila:
        
        print(elemento*valor_escalar, end=" ")
    
    print()
