"""
8- Reemplaza todas las vocales a de una cadena ingresada por teclado por una vocal e.
"""
ingresado = input("ingrese una cadena")
largo = len(ingresado)
"""
nueva = ""
for i in range(0,largo,1):
    if ingresado[i] != "a":
        nueva = nueva + ingresado[i]
    elif ingresado[i] == "a":
        nueva = nueva + "e"

print(nueva)
"""

print(ingresado)
remplazados = ingresado.replace("a","e")
print(remplazados)