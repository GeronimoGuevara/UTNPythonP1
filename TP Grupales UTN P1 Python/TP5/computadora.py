from componente_cpu import ComponenteCPU

class Computadora:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.componentes = []

    def agregar_componente(self, componente: ComponenteCPU):
        self.componentes.append(componente)

    def calcular_costo_total(self):
        return sum(componente.calcular_subtotal() for componente in self.componentes)

    def calcular_precio_venta(self):
        costo_total = self.calcular_costo_total()
        if costo_total < 50000:
            return costo_total * 1.40
        else:
            return costo_total * 1.30

    def __str__(self):
        componentes_str = "\n".join([str(comp) for comp in self.componentes])
        costo_total = self.calcular_costo_total()
        precio_venta = self.calcular_precio_venta()
        return (f"Marca: {self.marca}\nModelo: {self.modelo}\nComponentes:\n{componentes_str}\n"
                f"Costo Total: ${costo_total}\nPrecio de venta sugerido: ${precio_venta}")
