"""1. Codifique la clase celda con los atributos: 
fila; //entero 
columna; //entero 
valor; //cadena 
 Crea una clase Matriz que contenga una variable celdas 
celdasMatriz = []; 
 Codifique un programa que solicite al usuario un valor para la celda y que solicite la 
posición donde se desea almacenar el valor, cree una instancia de la clase Celda, 
asigne los valores cargados por el usuario (fila, columna y valor) y agregue la 
instancia a la lista celdasMatriz; repita este proceso hasta que el usuario ingrese 
como valor la cadena “FIN”. Valide que la celda creada ya no exista anteriormente 
es decir si la fila y columna indicados ya fueron cargados en celdasMatriz. 
 Muestre por pantalla los valores cargados en la lista celdas.  
 Codifique un método que reciba como parámetro los valores fila y columna y 
retorne el valor almacenado en la Celda correspondiente, en caso de que la fila y la 
columna no exista retorne el mensaje “La fila y columna indicada no ha sido 
asignada en ninguna celda”"""
class Coche: 
    def __init__(self, marca, modelo, velocidad_maxima): 
        self.marca = marca 
        self.__modelo = modelo  # Atributo privado 
        self._velocidad_maxima = velocidad_maxima  # Atributo protegido 
 
    def mostrar_modelo(self): 
        print(f"El modelo es {self.__modelo}") 

 
# Instanciando la clase 
mi_coche = Coche("Toyota", "Corolla", 180) 
mi_coche.mostrar_modelo()  # "El modelo es Corolla" 
# Intentar acceder directamente al atributo privado genera un error: 
print(mi_coche._velocidad_maxima)  # AttributeError 