
from zooAnimales.animal import Animal

class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def cantidad_total_animales(self):
        print(Animal.total_animales())

    def agregar_zona(self, zona):
        self.zonas.append(zona)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre