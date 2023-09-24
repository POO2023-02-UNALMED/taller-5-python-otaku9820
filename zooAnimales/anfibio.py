
from zooAnimales.animal import Animal

class Anfibio(Animal):
    listado = []

    def __init__(self, nombre, edad, habitat, genero, color_piel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.color_piel = color_piel
        self.venenoso = venenoso
        Anfibio.listado.append(self)

    @staticmethod
    def cantidad_anfibios():
        return len(Anfibio.listado)

    def movimiento(self):
        return "saltar"

    @staticmethod
    def crear_rana(nombre, edad, genero):
        nuevo_anfibio = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        return nuevo_anfibio

    @staticmethod
    def crear_salamandra(nombre, edad, genero):
        nuevo_anfibio = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        return nuevo_anfibio

    def get_color_piel(self):
        return self.color_piel

    def set_color_piel(self, color_piel):
        self.color_piel = color_piel

    def is_venenoso(self):
        return self.venenoso

    def set_venenoso(self, venenoso):
        self.venenoso = venenoso