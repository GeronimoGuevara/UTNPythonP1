from habitacion import Habitacion

class Vivienda:
    def __init__(self, calle: str, numero: int, manzana: str, nro_casa: int, superficie_terreno: float):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nro_casa = nro_casa
        self.superficie_terreno = superficie_terreno
        self.habitaciones = []

    def agregar_habitacion(self, habitacion: Habitacion):
        self.habitaciones.append(habitacion)

    def getMetrosCuadradosCubiertos(self):
        metros_cubiertos = sum(habitacion.metros_cuadrados for habitacion in self.habitaciones)
        if metros_cubiertos > self.superficie_terreno:
            raise ValueError("La superficie cubierta no puede ser mayor a la superficie del terreno")
        return metros_cubiertos

    def __str__(self):
        return (f"Vivienda en Calle {self.calle} {self.numero}, Manzana {self.manzana}, Casa {self.nro_casa}\n"
                f"Superficie Terreno: {self.superficie_terreno}\nMetros Cuadrados Cubiertos: {self.getMetrosCuadradosCubiertos()}")
