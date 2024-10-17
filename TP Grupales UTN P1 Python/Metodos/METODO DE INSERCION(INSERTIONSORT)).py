#Metodo InsertionSort.....
lista = [123,4,6,45,234,733,113,112,43,64,87]
def insertionsort(lista): 
    print("El vector a ordenar con inserción es:", lista)
    lenght = len(lista)
    print("el largo de la lista vectorins == ",lenght)

    for i in range(1, lenght): 
        elemento = lista[i] 
        j = i-1
        while j >= 0 and elemento < lista[j] : 
                lista[j+1] = lista[j] 
                j -= 1
        lista[j+1] = elemento 

    print("El vector ordenado con inserción es: ", lista)

insertionsort(lista)