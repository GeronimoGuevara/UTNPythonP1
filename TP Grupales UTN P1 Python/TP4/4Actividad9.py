"""Dado el siguiente texto:
texto = "manzana naranja manzana pera pera pera naranja manzana"
a) Escribe un programa que cuente cuántas veces aparece cada palabra en el
texto utilizando un diccionario.
b) Imprime el diccionario resultante."""

texto = "manzana naranja manzana pera pera pera naranja manzana"
diccionario = texto.split()
conteo_palabra = {}
for palabra in diccionario:
    if palabra in conteo_palabra:
        conteo_palabra[palabra] += 1
    else:
        conteo_palabra[palabra] = 1

print(conteo_palabra)


