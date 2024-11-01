from Ingrediente import Ingrediente

class Plato:
    def __init__(self, nombre_completo: str, precio: float, es_bebida: bool):
        self.nombre_completo = nombre_completo
        self.precio = precio
        self.es_bebida = es_bebida
        self.ingredientes = []

    def agregar_ingrediente(self, ingrediente: Ingrediente):
        self.ingredientes.append(ingrediente)
