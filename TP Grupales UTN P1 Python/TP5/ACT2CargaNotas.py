from Alumno import Alumno
from Nota import Nota

class CargaNotas:
    @staticmethod
    def main():
        alumnos = []
        
        while True:
            print("INGRESE DATOS DEL ALUMNO")
            nombre_completo = input("Ingrese nombre completo: ")
            legajo = int(input("Ingrese legajo: "))
            alumno = Alumno(nombre_completo, legajo)
            
            while True:
                print("INGRESE DATOS DE LA NOTA")
                catedra = input("Ingrese nombre de la cátedra: ")
                nota_examen = float(input("Ingrese la nota del examen: "))
                nota = Nota(catedra, nota_examen)
                
                alumno.agregar_nota(nota)
                
                salir_notas = input("¿Desea salir de la carga de notas? (s/n): ").lower()
                if salir_notas == 's' and len(alumno.notas) > 0:
                    break
                elif salir_notas == 's' and len(alumno.notas) == 0:
                    print("Debe ingresar al menos una nota.")
            
            alumnos.append(alumno)
            
            salir_alumno = input("¿Desea salir de la carga de alumnos? (s/n): ").lower()
            if salir_alumno == 's':
                break
        
        for alumno in alumnos:
            print("\nDatos del Alumno:")
            print(f"Nombre: {alumno.nombre_completo}")
            print(f"Legajo: {alumno.legajo}")
            print("Notas:")
            for nota in alumno.notas:
                print(f"Cátedra: {nota.catedra}, Nota: {nota.nota_examen}")
            print(f"Promedio del Alumno: {alumno.calcular_promedio()}")

if __name__ == "__main__":
    CargaNotas.main()
