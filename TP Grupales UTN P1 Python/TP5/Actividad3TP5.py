class Ingrediente:
    def __init__(self, nombre: str, cantidad: float, unidad_medida: str):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida

    def __str__(self):
        return f"{self.nombre} {self.cantidad} {self.unidad_medida}"


class Plato:
    def __init__(self, nombre_completo: str, precio: float, es_bebida: bool):
        self.nombre_completo = nombre_completo
        self.precio = precio
        self.es_bebida = es_bebida
        self.ingredientes = []

    def agregar_ingrediente(self, ingrediente: Ingrediente):
        self.ingredientes.append(ingrediente)

    def __str__(self):
        ingredientes_str = "\n".join([str(ing) for ing in self.ingredientes]) if not self.es_bebida else "No aplica"
        return (f"{self.nombre_completo}\nPrecio: ${self.precio}\n"
                f"Ingredientes:\n{ingredientes_str}\n{'-' * 40}")


class MenuRestaurant:
    def __init__(self):
        self.platos_menu = []

    def cargar_platos(self):
        while True:
            nombre_completo = input("Ingrese el nombre del plato: ")
            precio = float(input("Ingrese el precio del plato: "))
            es_bebida = input("¿Es una bebida? (s/n): ").strip().lower() == 's'

            plato = Plato(nombre_completo, precio, es_bebida)

            if not es_bebida:
                while True:
                    nombre_ingrediente = input("Ingrese el nombre del ingrediente: ")
                    cantidad = float(input("Ingrese la cantidad: "))
                    unidad_medida = input("Ingrese la unidad de medida: ")

                    ingrediente = Ingrediente(nombre_ingrediente, cantidad, unidad_medida)
                    plato.agregar_ingrediente(ingrediente)

                    agregar_mas = input("¿Agregar otro ingrediente? (s/n): ").strip().lower()
                    if agregar_mas != 's':
                        break

            self.platos_menu.append(plato)

            agregar_otro = input("¿Desea agregar otro plato? (s/n): ").strip().lower()
            if agregar_otro != 's':
                break

    def mostrar_menu(self):
        print("-----------MENÚ----------------")
        for plato in self.platos_menu:
            print(plato)

    @staticmethod
    def main():
        menu = MenuRestaurant()
        menu.cargar_platos()
        menu.mostrar_menu()

if __name__ == "__main__":
    MenuRestaurant.main()
