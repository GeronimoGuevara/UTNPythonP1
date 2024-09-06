"""
12- Dada la cadena “hipopotamo”, extraer la cuarta y quinta letra. 
"""

cadena = "hipopotamo"
extraido = ""
nueva = ""

for i in range(len(cadena)):
    if i == 3 or i == 4:
        extraido = extraido + cadena[i]
    else:
        nueva = nueva + cadena[i]


print(extraido)
print(nueva)