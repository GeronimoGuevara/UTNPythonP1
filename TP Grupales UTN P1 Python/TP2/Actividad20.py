#Cree una clase Fracción con dos atributos, numerador y denominador. 
#Agregue a la clase los siguientes 4 métodos e implemente los mismos: 
#sumarFracciones(Fraccion f1, Fraccion f2) 
#restarFracciones(Fraccion f1, Fraccion f2) 
#multiplicarFracciones(Fraccion f1, Fraccion f2) 
#dividirFracciones(Fraccion f1, Fraccion f2)
#Todos los métodos deben retornar la fracción resultante de la operación.

#Cree una clase OperacionesFraccion que contenga un método main donde se solicite
#al usuario el ingreso de 4 valores numéricos enteros con los cuales se crearan 2 objetos
#Fracción y finalizada la creación de los mismos se ejecutaran los 4 métodos
#implementados anteriormente asignando el resultado a una nueva variable de tipo
#Fracción y mostrando por pantalla el resultado de las operaciones realizadas.

class Fraccion:
    
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        
        
    def simplificar(a,b):
        while b != 0:
            aux = b
            b = a % b
            a = aux
            
        return a
        
        
    def sumarFracciones(f1,f2):
    
        num = (f1.numerador * f2.denominador) + (f2.numerador * f1.denominador)
        den = f1.denominador * f2.denominador
        mcDivisor = Fraccion.simplificar(num,den)
        
        return f"SUMA: {num//mcDivisor}/{den//mcDivisor}"
        
            
    def restarFracciones(f1,f2):
        
        num = (f1.numerador * f2.denominador) - (f2.numerador * f1.denominador)
        den = f1.denominador * f2.denominador
        mcDivisor = Fraccion.simplificar(num,den)
        
        return f"RESTA: {num//mcDivisor}/{den//mcDivisor}"
            
    def multiplicarFracciones(f1,f2):
        
        num = f1.numerador * f2.numerador
        den = f1.denominador * f2.denominador
        mcDivisor = Fraccion.simplificar(num,den)
        
        return f"MULTIPLICACIÓN: {num//mcDivisor}/{den//mcDivisor}"
            
    def dividirFracciones(f1,f2):
            
        num = f1.numerador * f2.denominador
        den = f1.denominador * f2.numerador
        mcDivisor = Fraccion.simplificar(num,den)
        
        return f"DIVISIÓN: {num//mcDivisor}/{den//mcDivisor}"
            
class OperacionesFraccion:
    
    def main():
        
        numerador1 = int(input("Ingrese el primer numerador "))
        denominador1 = int(input("Ingrese el primer denominador "))
        numerador2 = int(input("Ingrese el segundo numerador "))
        denominador2 = int(input("Ingrese el segundo denominador "))
        
        f1 = Fraccion(numerador1,denominador1)
        f2 = Fraccion(numerador2,denominador2)
        
        suma = Fraccion.sumarFracciones(f1, f2)
        resta = Fraccion.restarFracciones(f1, f2)
        multiplicacion = Fraccion.multiplicarFracciones(f1, f2)
        division = Fraccion.dividirFracciones(f1, f2)
        
        print(suma)
        print(resta)
        print(multiplicacion)
        print(division)
        
#Ejecutar
OperacionesFraccion.main()
