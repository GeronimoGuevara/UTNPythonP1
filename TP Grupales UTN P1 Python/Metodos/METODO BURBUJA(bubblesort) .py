from random import sample 
lista = list(range(100)) 
vectorbs = sample(lista,8) 


def bubblesort(vectorbs):
    """Esta función ordenara el vector que le pases como argumento con el Método de Bubble Sort"""
    
    print("El vector a ordenar es:",vectorbs)
    n = 0 
    



    for _ in vectorbs:
        n += 1 
    
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            # Revisa la matriz de 0 hasta n-i-1
            if vectorbs[j] > vectorbs[j+1] :
                vectorbs[j], vectorbs[j+1] = vectorbs[j+1], vectorbs[j]
            # Se intercambian si el elemento encontrado es mayor 
            # Luego pasa al siguiente



            
    print ("El vector ordenado es: ",vectorbs)

bubblesort(vectorbs)
