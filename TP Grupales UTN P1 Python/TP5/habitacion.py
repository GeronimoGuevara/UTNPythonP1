class Habitacion:
    def __init__(self, nombre: str, metros_cuadrados: float):
        self.nombre = nombre
        self.metros_cuadrados = metros_cuadrados

    def __str__(self):
        return f"Habitación: {self.nombre}, Metros Cuadrados: {self.metros_cuadrados}"
