from Nota import Nota

class Alumno:
    def __init__(self, nombre_completo: str, legajo: int):
        self.nombre_completo = nombre_completo
        self.legajo = legajo
        self.notas = []

    def agregar_nota(self, nota: Nota):
        self.notas.append(nota)

    def calcular_promedio(self) -> float:
        if len(self.notas) == 0:
            return 0
        total = sum(nota.nota_examen for nota in self.notas)
        return total / len(self.notas)
