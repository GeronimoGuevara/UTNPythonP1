matriz = [[(i+1)*3 if i == j else 0 for j in range(4)] for i in range(4)]

print("Matriz cuadrada:")
for fila in matriz:
    print(fila)

diagonal = []
for i in range(4):
    for j in range(4):
        
        if i == j:
            
            diagonal.append(matriz[i][j])

print()
print("Los elementos de la diagonal son: ")
print(diagonal)
