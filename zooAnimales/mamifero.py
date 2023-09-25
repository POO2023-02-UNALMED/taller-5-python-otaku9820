
from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero._listado)

    @classmethod
    def crearCaballo(cls,nombre, edad, genero):
        nuevo_mamifero = cls(nombre, edad, "pradera", genero, True, 4)
        cls.caballos += 1
        return nuevo_mamifero

    @classmethod
    def crearLeon(cls,nombre, edad, genero):
        nuevo_mamifero = cls(nombre, edad, "selva", genero, True, 4)
        cls.leones += 1
        return nuevo_mamifero

    def getPatas(self):
        return self._patas

    def setPatas(self, patas):
        self._patas = patas

    def isPelaje(self):
        return self._pelaje

    def setPelaje(self, pelaje):
        self._pelaje = pelaje