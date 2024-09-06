
numero = int(input(print("ingrese un numero para verificar si es primo o no: ")))
divisores = 0
if numero <= 1:
    print("El numero ingresado no es primo")

for i in range (2,numero+1):
    if (numero % i) == 0:
        divisores = divisores + 1

if divisores == 1:
    print("El numero ingresado es primo")
else:
    print("El numero ingresado no es primo")