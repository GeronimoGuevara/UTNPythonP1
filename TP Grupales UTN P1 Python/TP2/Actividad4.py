
class CantBilletes:
    def __init__(self, precio):

        self.precio = precio

        self.monedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05]

        self.resultado = {}


    def calculo(self):

        cantFalta = self.precio
        
        for i in self.monedas:
            if cantFalta >= i:
                cantB = cantFalta // i
                cantFalta = round(cantFalta % i, 2)
                self.resultado[i] = int(cantB)
            else:
                self.resultado[i] = 0

    def mostraResultado(self):
        for i, cantidad in self.resultado.items():
            if i >= 1:
                print(f"{cantidad} billetes de {i}")
            else:
                print(f"{cantidad} monedas de {i}")


                    
precio = float(input("Ingrese el precio del producto para ver cuantos billetes necesita: "))
CantBilletes(precio)

result = CantBilletes(precio)

result.calculo()

result.mostraResultado()
