"""
16- Codifique un método que reciba como parámetro una cadena y determine si la
misma contiene o no números
"""
def contiene_numeros(cadena):
    for i in cadena:
        if i.isdigit():
            return True
    return False

cadena = "Hola124"

print("La cadena ",cadena," contiene números:",contiene_numeros(cadena))