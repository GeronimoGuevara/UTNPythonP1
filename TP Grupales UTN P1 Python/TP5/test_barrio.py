from barrio import Barrio
from vivienda import Vivienda
from habitacion import Habitacion

def main():
    barrio = Barrio("Barrio Las Flores", "Constructora ABC")

    vivienda1 = Vivienda("Calle 1", 123, "A", 1, 150.0)
    vivienda1.agregar_habitacion(Habitacion("Sala", 40.0))
    vivienda1.agregar_habitacion(Habitacion("Cocina", 30.0))
    vivienda1.agregar_habitacion(Habitacion("Dormitorio", 50.0))

    vivienda2 = Vivienda("Calle 2", 456, "B", 2, 100.0)
    vivienda2.agregar_habitacion(Habitacion("Sala", 30.0))
    vivienda2.agregar_habitacion(Habitacion("Dormitorio", 40.0))

    barrio.agregar_vivienda(vivienda1)
    barrio.agregar_vivienda(vivienda2)

    print(barrio)
    print(f"Superficie Total de Terreno en Manzana A: {barrio.getSuperficieTotalTerrenoXManzana('A')}")
    print(f"Superficie Total de Terreno en Manzana B: {barrio.getSuperficieTotalTerrenoXManzana('B')}")

if __name__ == "__main__":
    main()
