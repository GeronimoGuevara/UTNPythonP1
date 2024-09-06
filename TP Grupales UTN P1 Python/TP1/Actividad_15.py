def multiplo_de_nueve(suma_digitos):
    return suma_digitos % 9 == 0

def multiplo_de_tres(suma_digitos):
    return suma_digitos % 3 == 0

def multiplo_de_dos(num):

    return int(num) % 2 == 0


# Para los cuales hay que saber su ultimo digito
def obtener_ultimo_digito(num):
    ultimo_digito = int(num) % 10
    
    return ultimo_digito


# Para los cuales hay que sumar sus crifras
def sumar_cifras(num):
    
    # En esta variable se ira almacenando la suma de los digitos
    suma_digitos = 0

    # Por cada digito del numero
    for digito in num:
        # Convertir el dígito a un entero y sumarlo
        suma_digitos += int(digito)
        
    return suma_digitos



print("CRITERIOS DE DIVISIBILIDAD")
num=input("Ingrese un numero ")


# Funcion para obtener la suma de las cifras  
suma_digitos = sumar_cifras(num)
# Funcion para obtener el ultimo digito del numero
ultimo_digito = obtener_ultimo_digito(num)


# 2
if multiplo_de_dos(num):
    print("Cumple con el criterio de divisibilidad del 2")

# 3
if multiplo_de_tres(suma_digitos):
    print("Cumple con el criterio de divisibilidad del 3")

# 5
if ultimo_digito == 0 or ultimo_digito == 5:
        print("Cumple con el criterio de divisibilidad del 5")
     
# 6
if multiplo_de_dos(num) and multiplo_de_tres(suma_digitos):
        print("Cumple con el criterio de divisibilidad del 6")
        
# 9
if multiplo_de_nueve(suma_digitos):
    print("Cumple con el criterio de divisibilidad del 9")
    
# 10
if ultimo_digito == 0:
    print("Cumple con el criterio de divisibilidad del 10")
