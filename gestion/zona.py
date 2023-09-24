

class Zona:
    def __init__(self, nombre, zoo=None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def agregarAnimal(self, animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        print(len(self.animales))

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getZoo(self):
        return self.zoo

    def setZoo(self, zoo):
        self.zoo = zoo
