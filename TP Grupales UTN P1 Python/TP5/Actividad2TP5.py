class Nota:
    def __init__(self):

        self.materiaNota = []
        
    def agregarNotas(self,catedra,notaExamen):
        self.materiaNota.append({"Catedra" : catedra, "Nota Examen" : notaExamen})

class Alumno(Nota):
    def __init__(self,nombreCompleto,legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = Nota()

    def agregarNotas(self, catedra, notaExamen):
        self.notas.agregarNotas(catedra, notaExamen)

    def agregarAlDiccionario(self):
        infoAlumno = {
            "nombre" : self.nombreCompleto, 
            "Legajo" : self.legajo, 
            "Notas" : self.notas.materiaNota
        }
        return infoAlumno        

class CargaNotas:
    def __init__(self):
        self.Main()

    def Main(self):

        print("Cargando notas...")
        self.alumnos = []
        while True:
            print("Ingrese los datos del alumno.")
            nombreCompleto = str(input("Ingrese el numbre completo:(no ingrese nada para finalizar la carga) "))
            if not nombreCompleto:
                break

            legajo = int(input("Ingrese el numero de legajo del alumno: "))
            alumno = Alumno(nombreCompleto,legajo)            
            cantNotas = int(input("Ingrese la cantidad de notas que va a ingresar para ese alumno: "))
            sumanotas = 0
            if cantNotas < 1:
                print("Usted no puede no ingresar notas")
                break

            for i in range(cantNotas):
                catedra = str(input(f"Ingrese el nombre de la materia {i+1}: "))
                nota = float(input(f"Ingrese la nota numero {i+1}: "))
                alumno.agregarNotas(catedra,nota)
                sumanotas += nota

            self.alumnos.append(alumno.agregarAlDiccionario())

            promedio = sumanotas / cantNotas

        print("Carga finalizada. Lista de alumnos: ")
        for i in self.alumnos:
            print(f"\nNombre del alumno: {i['nombre']}\nLegajo del alumno: {i['Legajo']}")
            for nota in i['Notas']:
                print(f"Materia: {nota['Catedra']}, Nota: {nota['Nota Examen']}")

if __name__ == "__main__":
    CargaNotas()
