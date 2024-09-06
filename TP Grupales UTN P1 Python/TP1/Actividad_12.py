#ACTIVIDAD12

def switch_case(case):
    match case:
        case '1':
            print("Hoy es lunes, SI es dia laboral")
        case '2':
            print("Hoy es martes, SI es dia laboral")
        case '3':
            print("Hoy es miercoles, SI es dia laboral")
        case '4':
            print("Hoy es jueves, SI es dia laboral")
        case '5':
            print("Hoy es viernes, SI es dia laboral")
        case '6':
            print("Hoy es sabado, NO es dia laboral")
        case "7":
            print("Hoy es domingo, NO es dia laboral")
        case _:
            print("Usted no ingreso un dia de la semana")

opcion = input("Ingrese un dia de la semana del 1 al 7 ")
switch_case(opcion)
