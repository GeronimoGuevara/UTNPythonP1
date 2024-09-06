"""
9- Recorre la cadena del ejercicio 6 y transforma cada carácter a su código ASCII.
Muéstralos en línea recta, separados por un espacio entre cada carácter. 
"""
cadena = "La lluvia en Mendoza es escasa"
valores_ascii = ""

for i in range(0,len(cadena)):
    valores_ascii = valores_ascii + str(ord(cadena[i])) + " "

print("Valores ASCII:", valores_ascii)
