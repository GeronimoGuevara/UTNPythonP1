#ACTIVIDAD 2
"""
2- Si se asigna un valor a una variable fuera de rango (mayor de lo establecido) ¿Qué
ocurre? ¿Existe alguna forma de resolverlo? Ejemplifique. 

Si se asigna un valor a una variable fuera de rango nos arrojara un index error diciendo que nos excedimos del rango y para solucionarlo podemos utilizar el len() para conocer la longitud de la variable y remplazar el valor por esa longitud -1 

"""
lista = [1,3,6,"Gero"]
#si le decimos que escriba el elemento numero 4 de la lista nos mostrara el error
#print(lista[4])

"""
si modificamos el codigo y le decimos que nos diga la longitud de la lista 
"""
longitud = len(lista)
print(longitud)
# y ahora si podemos decirle al programa que imprima la longitud de la lista menos 1 para que funcione el codigo si no le ponemos el -1 volvera a arrojar el error por que en las listas se cuenta el 0 como primer elemento no el 1 

print(lista[longitud-1])

