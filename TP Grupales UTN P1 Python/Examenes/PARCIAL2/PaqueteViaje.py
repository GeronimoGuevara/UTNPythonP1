class PaqueteViaje:
    def __init__(self,nombre):
        self.nombre = nombre
        self.dias = []
        self.costoTotal = 0.0

    def agregarDias(self,dia):
        self.dias.append(dia)
    

    def totalCostoViaje(self):
        for dia in self.dias:
            for ciudad in self.ciudad:
                for actividad in self.actividad:
                    self.costoTotal += actividad.costoActividad
        return self.costoTotal
    
