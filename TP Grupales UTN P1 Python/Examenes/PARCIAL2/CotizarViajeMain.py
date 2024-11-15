from PaqueteViaje import PaqueteViaje
from DiaViaje import DiaViaje
from Ciudad import Ciudad
from Actividad import Actividad

class CotizarViaje:
    def __init__(self):
        self.costoActividades = [
            {"codigo": 100, "actividad": "DESAYUNO", "costo_estandar": 3000, "costo_exclusive": 4000},
            {"codigo": 200, "actividad": "ALMUERZO", "costo_estandar": 8000, "costo_exclusive": 9000},
            {"codigo": 300, "actividad": "MEDIATARDE", "costo_estandar": 4000, "costo_exclusive": 5000},
            {"codigo": 400, "actividad": "CENA", "costo_estandar": 7000, "costo_exclusive": 8000},
            {"codigo": 500, "actividad": "HOTEL 3 ESTRELLAS", "costo_estandar": 25000, "costo_exclusive": 27000},
            {"codigo": 600, "actividad": "HOTEL 4 ESTRELLAS", "costo_estandar": 30000, "costo_exclusive": 32000},
            {"codigo": 700, "actividad": "HOTEL 5 ESTRELLAS", "costo_estandar": 35000, "costo_exclusive": 38000},
            {"codigo": 800, "actividad": "VISITA MUSEO", "costo_estandar": 3500, "costo_exclusive": 4500},
            {"codigo": 900, "actividad": "CITY TOUR", "costo_estandar": 5500, "costo_exclusive": 7500},
        ]

    def crearPaquete(self):
        nombre = input("Ingrese el nombre del paquete de viaje: ")
        paqueteViaje = PaqueteViaje(nombre)

        cantDias = int(input("Ingrese la cantidad de dias del viaje: "))
        while cantDias < 7 or cantDias > 30:
            print("La cantidad de dias debe ser entre 7 y 30")
            cantDias = int(input("Ingrese la cantidad de dias del viaje: "))
        
        for i in range(cantDias):
            dia = DiaViaje(i + 1)
            cantCiudades = int(input(f"Ingrese la cantidad de ciudades para el día {i + 1}: "))

            for j in range(cantCiudades):
                nombreCiudad = input(f"Ingrese la ciudad {j + 1} del día {i + 1}: ")
                nombrePais = input(f"Ingrese el nombre del pais de la ciudad {j + 1}: ")
                ciudad = Ciudad(nombreCiudad, nombrePais)

                cantActividades = int(input("Ingrese la cantidad de actividades a realizar: "))
                while cantActividades < 3:
                    print("La cantidad de actividades debe ser al menos 3")
                    cantActividades = int(input("Ingrese la cantidad de actividades a realizar: "))
                
                print("Seleccione una actividad de la lista: ")
                for actividad in self.costoActividades:
                    print(f"{actividad['codigo']}: {actividad['actividad']}")

                for x in range(cantActividades):
                    codigoActividad = int(input("Ingrese el codigo de una de las actividades: "))
                    tipo = input("Ingrese el tipo de actividad S (standard) o E (exclusive): ").upper()

                    while tipo not in ("S", "E"):
                        print("Opcion ingresada incorrecta, ingrese S o E")
                        tipo = input("Ingrese el tipo de actividad S (standard) o E (exclusive): ").upper()
                    
                    for actividad in self.costoActividades:
                        if actividad["codigo"] == codigoActividad:
                            costo = actividad["costo_estandar"] if tipo == "S" else actividad["costo_exclusive"]
                            ciudad.agregarActividades(Actividad(actividad["actividad"], tipo, costo))
                            break

                dia.agregarCiudad(ciudad)
            paqueteViaje.agregarDias(dia)
        
        return paqueteViaje

    def mostrarInfo(self, paqueteViaje):
        print("---------------Paquete---------------")
        print(f"Nombre del paquete: {paqueteViaje.nombre}")
        print(f"Cantidad de dias: {len(paqueteViaje.dias)}")
        print("---------------Dias---------------")
        
        for dia in paqueteViaje.dias:
            print(f"Dia: {dia.numeroDia}")
            print("---------------Ciudades---------------")
            for ciudad in dia.listaCiudades:
                print(f"Ciudad: {ciudad.nombreCiudad}")
                print(f"Pais: {ciudad.nombrePais}")
                print("---------------Actividades---------------")
                total_costo_actividades = sum(actividad.costoActividad for actividad in ciudad.listaActividades)
                for actividad in ciudad.listaActividades:
                    print(f"Actividad: {actividad.tipoActividad}, Tipo: {actividad.tipo}, Costo: {actividad.costoActividad}")
                print("Costo Total de Actividades:", total_costo_actividades)

        print("-------------------------------------------")
        print("Costo Total del Viaje:", paqueteViaje.totalCostoViaje())
        print("Costo Promedio Por Dia:", paqueteViaje.totalCostoViaje() / len(paqueteViaje.dias))

    @staticmethod
    def main():
        cotizarViaje = CotizarViaje()
        paqueteViaje = cotizarViaje.crearPaquete()
        cotizarViaje.mostrarInfo(paqueteViaje)


if __name__ == "__main__":
    CotizarViaje.main()
