
from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas=0
    salamandras=0

    def __init__(self, nombre, edad, habitat, genero, color_piel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._color_piel = color_piel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio._listado)

    def movimiento(self):
        return "saltar"

    @staticmethod
    def crear_rana(cls, nombre, edad, genero):
        cls(nombre, edad,"selva", genero,"rojo", True)
        cls.ranas+=1

    @staticmethod
    def crearSalamandra(cls, nombre, edad, genero):
         cls(nombre, edad, "selva", genero, "negro y amarillo", False)
         cls.salamandras +=1

    def getColorPiel(self):
        return self._color_piel

    def setColorPiel(self, color_piel):
        self._color_piel = color_piel

    def isVenenoso(self):
        return self.venenoso

    def setVenenoso(self, venenoso):
        self.venenoso = venenoso