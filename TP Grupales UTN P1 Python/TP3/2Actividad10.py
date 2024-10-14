lista = [[1,2,3],
        [2,5,6],
        [3,6,9]]

subLista = []
lista2= [[],[],[]]

def transponer(lista):
    global lista2
    for fila in lista:
        for indice,item in enumerate(fila):
            lista2[indice].append(item)
    return lista2


transponer(lista)


def iguales(lista2):

    print(lista2)
    print(lista == lista2)
    if lista2 == lista:
        print("son iguales")
    else:
        print("no son iguales")


iguales(lista2)