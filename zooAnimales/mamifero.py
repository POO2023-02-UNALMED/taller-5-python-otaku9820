
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
    def cantidadMamiferos():
        return len(Mamifero.listado)

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        nuevo_mamifero = Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.caballos += 1
        return nuevo_mamifero

    @staticmethod
    def crearLeon(nombre, edad, genero):
        nuevo_mamifero = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones += 1
        return nuevo_mamifero

    def getPatas(self):
        return self.patas

    def setPatas(self, patas):
        self.patas = patas

    def isPelaje(self):
        return self.pelaje

    def setPelaje(self, pelaje):
        self.pelaje = pelaje