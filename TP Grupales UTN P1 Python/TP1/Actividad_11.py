#ACTIVIDAD 11
contraseña= "46621624"
intentos = int(0)
while True:
    ingreso= input(print("ingrese la contraseña: "))
    if ingreso == contraseña:
        print("Acceso Correcto")
        break
    else:
        if intentos == 2:
            print("se ha bloqueado el acceso excedio el limite de intentos")
            break
    intentos = intentos + 1
