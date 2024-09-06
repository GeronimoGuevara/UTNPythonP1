import random

numero_aleatorio= random.randint(0,100)
cant_intentos = 0

print("El numero aleatorio es: ",numero_aleatorio)
while True:
    print("Ingrese un numero entre el 0 y 100")
    intentos= int(input("Numero: "))
    cant_intentos = cant_intentos + 1
    if intentos == numero_aleatorio:
        print("Correcto el numero era: ",numero_aleatorio)
        print("Cantidad de intentos utilizados: ", cant_intentos)
        break

    else:
        if intentos<numero_aleatorio:
            print("Mas alto")
        else:
            print("Mas bajo")

            