from computadora import Computadora
from componente_cpu import ComponenteCPU

class CostoComputadora:
    @staticmethod
    def main():
        while True:
            marca = input("Ingrese la marca de la computadora: ")
            modelo = input("Ingrese el modelo de la computadora: ")
            computadora = Computadora(marca, modelo)

            while True:
                componente = input("Ingrese el nombre del componente: ")
                marca_componente = input("Ingrese la marca del componente: ")
                cantidad = int(input("Ingrese la cantidad del componente: "))
                precio = float(input("Ingrese el precio por unidad del componente: "))

                componente_cpu = ComponenteCPU(componente, marca_componente, cantidad, precio)
                computadora.agregar_componente(componente_cpu)

                agregar_mas = input("¿Agregar otro componente? (s/n): ").strip().lower()
                if agregar_mas != 's':
                    break

            print("-----------Computadora----------------")
            print(computadora)

            nueva_cotizacion = input("¿Desea cotizar una nueva computadora? (s/n): ").strip().lower()
            if nueva_cotizacion != 's':
                print("Fin de la cotización.")
                break

if __name__ == "__main__":
    CostoComputadora.main()
