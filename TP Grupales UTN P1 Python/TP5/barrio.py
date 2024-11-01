from vivienda import Vivienda

class Barrio:
    def __init__(self, nombre: str, empresa_constructora: str):
        self.nombre = nombre
        self.empresa_constructora = empresa_constructora
        self.viviendas = []

    def agregar_vivienda(self, vivienda: Vivienda):
        self.viviendas.append(vivienda)

    def getSuperficieTotalTerreno(self):
        return sum(vivienda.superficie_terreno for vivienda in self.viviendas)

    def getSuperficieTotalTerrenoXManzana(self, manzana: str):
        return sum(vivienda.superficie_terreno for vivienda in self.viviendas if vivienda.manzana == manzana)

    def getSuperficieTotalCubierta(self):
        total_cubierta = 0
        for vivienda in self.viviendas:
            total_cubierta += vivienda.getMetrosCuadradosCubiertos()
        return total_cubierta

    def __str__(self):
        return (f"Barrio: {self.nombre}\nEmpresa Constructora: {self.empresa_constructora}\n"
                f"Superficie Total Terreno: {self.getSuperficieTotalTerreno()}\n"
                f"Superficie Total Cubierta: {self.getSuperficieTotalCubierta()}")
