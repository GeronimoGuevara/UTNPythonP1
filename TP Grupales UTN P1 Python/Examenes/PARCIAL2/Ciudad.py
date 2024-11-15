class Ciudad:
    def __init__(self,nombreCiudad,nombrePais):
        self.nombreCiudad = nombreCiudad
        self.nombrePais = nombrePais
        self.listaActividades = []
        
    def agregarActividades(self,actividad):
        if actividad not in self.listaActividades:
            self.listaActividades.append(actividad)
        else:
            print("La actividad ya se encuentra en la lista de actividades de la ciudad")


    def totalActividades(self):
        return len(self.listaActividades)

