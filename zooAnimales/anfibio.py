
from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, color_piel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.color_piel = color_piel
        self.venenoso = venenoso
        Anfibio.listado.append(self)

    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio.listado)

    def movimiento(self):
        return "saltar"

    @staticmethod
    def crear_rana(nombre, edad, genero):
        nuevo_anfibio = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        return nuevo_anfibio

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        nuevo_anfibio = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        return nuevo_anfibio

    def getColorPiel(self):
        return self.color_piel

    def setColorPiel(self, color_piel):
        self.color_piel = color_piel

    def isVenenoso(self):
        return self.venenoso

    def setVenenoso(self, venenoso):
        self.venenoso = venenoso