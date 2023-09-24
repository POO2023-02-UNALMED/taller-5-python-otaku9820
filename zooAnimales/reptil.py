
from zooAnimales.animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, color_escamas, largo_cola):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = color_escamas
        self.largoCola = largo_cola
        Reptil.listado.append(self)

    @staticmethod
    def cantidadReptiles():
        return len(Reptil.listado)

    def movimiento(self):
        return "reptar"

    @staticmethod
    def crearIguana(nombre, edad, genero):
        nuevo_reptil = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.iguanas += 1
        return nuevo_reptil

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        nuevo_reptil = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.serpientes += 1
        return nuevo_reptil

    def getColorEscamas(self):
        return self.color_escamas

    def setColorEscamas(self, color_escamas):
        self.colorEscamas = color_escamas

    def getLargoCola(self):
        return self.largoCola

    def setLargoCola(self, largo_cola):
        self.largoCola = largo_cola