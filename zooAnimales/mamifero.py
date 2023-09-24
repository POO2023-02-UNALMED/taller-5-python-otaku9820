
from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)

    @staticmethod
    def cantidad_mamiferos():
        return len(Mamifero.listado)

    @staticmethod
    def crear_caballo(nombre, edad, genero):
        nuevo_mamifero = Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.caballos += 1
        return nuevo_mamifero

    @staticmethod
    def crear_leon(nombre, edad, genero):
        nuevo_mamifero = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones += 1
        return nuevo_mamifero

    def get_patas(self):
        return self.patas

    def set_patas(self, patas):
        self.patas = patas

    def is_pelaje(self):
        return self.pelaje

    def set_pelaje(self, pelaje):
        self.pelaje = pelaje