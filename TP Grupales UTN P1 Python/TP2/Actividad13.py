"""
13- Pedir el ingreso de dos cadenas por por teclado, indicar si la segunda cadena se
encuentra dentro de la primera. 
"""
cadena1 = input("ingrese una cadena")
cadena2 = input("ingrese una cadena2")
valor = cadena1.find(cadena2)
valor2 = cadena2.find(cadena1)

if valor >= 0:
    print("la cadena 1 contiene a la cadena 2")
elif valor <= 0:
    print("la cadena 1 no contiene a la cadena 2")


if valor2 >= 0:
        print("la cadena 2 contiene a la cadena 1")
elif valor2 <= 0:
        print("la cadena 2 no contiene a la cadena 1")
