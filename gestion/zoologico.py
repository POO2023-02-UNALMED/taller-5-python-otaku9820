
from zooAnimales.animal import Animal 

class Zoologico:
    _zonas=[]
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        

    def cantidadTotalAnimales(self):
        print(Animal.total_animales())

    def agregarZona(self, zona):
        self.zonas.append(zona)

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre