#Cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un atributo de nombre operación.
#Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente:
#sumarNumeros()
#restarNumeros()
#multiplicarNumeros()
#dividirNumeros()
#El quinto método será el siguiente:
#aplicarOperacion(operacion){
#   …………………..
#}
#Cree una clase Calculo que contenga un método main, donde cree una instancia de la clase OperacionMatematica, 
#asigne 2 valores para las variables de la instancia y ejecute la función aplicarOperacion, 
#pasando como parámetro primero “+”, después “-”, a continuación “*” y finalmente “/”. 
#Muestre por pantalla el resultado de las operaciones.

class OperacionMatemática:
    
    def __init__(self, valor1, valor2, operacion):
        self.valor1 = valor1
        self.valor2 = valor2
        self.operacion = operacion
        
    def sumarNumeros(self):
        rdo = self.valor1 + self.valor2
        return rdo
    
    def restarNumeros(self):
        rdo = self.valor1 - self.valor2
        return rdo
    
    def multiplicarNumeros(self):
        
        rdo = self.valor1 * self.valor2
        return rdo
    
    def dividirNumeros(self):
        rdo = self.valor1 / self.valor2
        return rdo
        
        
    def aplicarOperacion(self):
        if self.operacion == "+":
            return self.sumarNumeros()
        
        if self.operacion == "-":
            return self.restarNumeros()
        
        if self.operacion == "*":
            return self.multiplicarNumeros()
        
        if self.operacion == "/":
            return self.dividirNumeros()
        
        
class Calculo:
    
    def main():
        
        valor1 = int(input("Ingrese el primer valor "))
        valor2 = int(input("Ingrese el segundo valor "))
        
        operaciones = [ "+" , "-" , "*" , "/" ]
        
        for signo in operaciones:
            resultado = OperacionMatemática(valor1,valor2,signo)
            print("El resultado de la ", signo, " es ", resultado.aplicarOperacion())
            
#Ejecutar
Calculo.main()
