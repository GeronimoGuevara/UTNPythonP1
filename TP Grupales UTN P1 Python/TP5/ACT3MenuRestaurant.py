from Plato import Plato
from Ingrediente import Ingrediente

class MenuRestaurant:
    @staticmethod
    def main():
        platos_menu = []
        
        while True:
            # Solicitar los datos del plato
            print("INGRESE DATOS DEL PLATO")
            nombre_completo = input("Ingrese el nombre del plato: ")
            precio = float(input("Ingrese el precio del plato: "))
            es_bebida = input("¿Es una bebida? (s/n): ").lower() == 's'
            plato = Plato(nombre_completo, precio, es_bebida)
            
            # Cargar ingredientes si no es bebida
            if not es_bebida:
                while True:
                    print("INGRESE DATOS DEL INGREDIENTE")
                    nombre_ingrediente = input("Nombre del ingrediente: ")
                    cantidad = float(input("Cantidad: "))
                    unidad_medida = input("Unidad de medida: ")
                    ingrediente = Ingrediente(nombre_ingrediente, cantidad, unidad_medida)
                    
                    # Agregar el ingrediente al plato
                    plato.agregar_ingrediente(ingrediente)
                    
                    salir_ingredientes = input("¿Desea salir de la carga de ingredientes? (s/n): ").lower()
                    if salir_ingredientes == 's' and len(plato.ingredientes) > 0:
                        break
                    elif salir_ingredientes == 's' and len(plato.ingredientes) == 0:
                        print("Debe ingresar al menos un ingrediente.")
            
            # Agregar el plato al menú
            platos_menu.append(plato)
            
            salir_plato = input("¿Desea salir de la carga de platos? (s/n): ").lower()
            if salir_plato == 's':
                break

        # Mostrar el menú del restaurant
        print("\n----------- MENÚ ----------------")
        for plato in platos_menu:
            print(f"\n{plato.nombre_completo}")
            print(f"Precio: $ {plato.precio}")
            if plato.es_bebida:
                print("Es una bebida.")
            else:
                print("Ingredientes:")
                for ingrediente in plato.ingredientes:
                    print(f" - {ingrediente.nombre}, {ingrediente.cantidad} {ingrediente.unidad_medida}")
            print("----------------------------------")

# Ejecutar el programa
if __name__ == "__main__":
    MenuRestaurant.main()
