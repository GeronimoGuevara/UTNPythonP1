 

Matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
transpuesta = [[Matriz[j][i] for j in range(len(Matriz))] for i in range(len(Matriz[0]))]
print("la matriz transpuesta es: ")
for i in transpuesta:
    print(i)
        