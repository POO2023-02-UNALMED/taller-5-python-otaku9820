

class Zona:
    def __init__(self, nombre, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def agregarAnimal(self, animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        print(len(self._animales))

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getZoo(self):
        return self._zoo

    def setZoo(self, zoo):
        self._zoo = zoo
