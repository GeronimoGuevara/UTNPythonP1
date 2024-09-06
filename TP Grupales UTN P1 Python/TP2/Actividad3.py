#ACTIVIDAD 3

def sumar_digitos(numero):
    if 100 <= numero <= 999:
        digito1 = numero % 10
        numero = numero // 10
        digito2 = numero % 10
        numero = numero // 10
        digito3 = numero % 10

        suma = digito1 + digito2 + digito3
        return suma
    
    else:
        print("el numero ingresado no es de 3 digitos")

numero = int(input("Ingrese un numero entre el 100 y el 999 incluidos:"))

resultado = sumar_digitos(numero)
print("La suma de los digitos es de: ", resultado)
