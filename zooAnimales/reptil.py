from gestion.zona import Zona
from zooAnimales.animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, color_escamas, largo_cola):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.largo_cola = largo_cola
        Reptil.listado.append(self)

    @staticmethod
    def cantidad_reptiles():
        return len(Reptil.listado)

    def movimiento(self):
        return "reptar"

    @staticmethod
    def crear_iguana(nombre, edad, genero):
        nuevo_reptil = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.iguanas += 1
        return nuevo_reptil

    @staticmethod
    def crear_serpiente(nombre, edad, genero):
        nuevo_reptil = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.serpientes += 1
        return nuevo_reptil

    def get_color_escamas(self):
        return self.color_escamas

    def set_color_escamas(self, color_escamas):
        self.color_escamas = color_escamas

    def get_largo_cola(self):
        return self.largo_cola

    def set_largo_cola(self, largo_cola):
        self.largo_cola = largo_cola