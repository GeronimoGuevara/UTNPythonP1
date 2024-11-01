class Celda:
    def __init__(self,fila,columna,valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor

    def mostrarValor (self):
        print(f"El valor ingresado es: {self.valor} en la fila {self.fila} y en la columna {self.columna}")

class Matriz():
    def __init__(self):
        self.celdasMatriz = []

    def agregarCelda(self,nuevaCelda):
        for celda in self.celdasMatriz:
            if celda.fila == nuevaCelda.fila and celda.columna == nuevaCelda.columna:
                print("Ya existe una celda en esa posicion")
                return False
        self.celdasMatriz.append(nuevaCelda)
        return True
    
    def mostrarMatriz(self):
        for celda in self.celdasMatriz:
            celda.mostrarValor()

    def obtenerValor (self,fila,columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return "La fila y columna no ha sido asignada"

matriz = Matriz()

while True:
    valor = input("Ingrese el valor que va a ingresar en la matriz (fin para finalizar)").upper()    
    if valor == "FIN":
        break
    
    fila = int(input("Ingrese la fila en la que lo va a posicionar a ese valor"))
    columna = int(input("Ingrese la columna en que lo ingresara"))

    nuevaCelda = Celda(fila,columna,valor)

    if matriz.agregarCelda(nuevaCelda):
        print("Celda agregada correctamente")

print("\n Celdas cargadas en la matriz: ")
matriz.mostrarMatriz()

fila = int(input("\n Ingrese la fila para consultar el valor: "))
columna = int(input("Ingrese la columna para consultar el valor: "))
resultado = matriz.obtenerValor(fila,columna)
print(f"Resultado de la consulta: {resultado}")


