lista = [[1,2,3],
        [2,5,6],
        [3,6,9]]

subLista = []
# lista2= [lista[2][0], lista[1][0],lista [0][0]]
lista2 = [[],[],[]]


for primerItem in reversed(lista):
    for i in range(len(primerItem)):
        lista2[i].append(primerItem[i])

for i in lista2:
    print(i)
#print(lista2)