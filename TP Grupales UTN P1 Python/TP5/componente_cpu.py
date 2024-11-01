class ComponenteCPU:
    def __init__(self, componente: str, marca: str, cantidad: int, precio: float):
        self.componente = componente
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio

    def calcular_subtotal(self):
        return self.cantidad * self.precio

    def __str__(self):
        return (f"{self.componente} | Marca: {self.marca} | Cantidad: {self.cantidad} "
                f"| Precio por unidad: ${self.precio} | Subtotal: ${self.calcular_subtotal()}")
