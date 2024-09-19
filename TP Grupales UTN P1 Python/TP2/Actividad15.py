"""
15- Indique que sucede si realizo la siguiente declaración de variable:
x = None print(x)
Explique y ejemplifique el uso de None
"""
#Si ejecutamos esa declaracion nos imprimira por pantalla none.
#El none se utiliza para darle valor nulo o ausencia de valor a una variable,
#se puede utilizar para inicializar una variable con un valor nulo, 
#para indicar que una variable no tiene un valor asignado o 
#que una función no devuelve un valor significativo.

#Por ejemplo:
nombre = str(input("ingrese un nombre"))
if nombre == "":
    nombre = None
print(nombre)