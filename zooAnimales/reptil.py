
from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, color_escamas, largo_cola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = color_escamas
        self._largoCola = largo_cola
        Reptil._listado.append(self)

    @staticmethod
    def cantidadReptiles():
        return len(Reptil._listado)

    def movimiento(self):
        return "reptar"

    @staticmethod
    def crearIguana(cls,nombre, edad, genero):
        nuevo_reptil = cls(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.iguanas += 1
        return nuevo_reptil

    @staticmethod
    def crearSerpiente(cls,nombre, edad, genero):
        nuevo_reptil = cls(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.serpientes += 1
        return nuevo_reptil

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, color_escamas):
        self._colorEscamas = color_escamas

    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largo_cola):
        self._largoCola = largo_cola