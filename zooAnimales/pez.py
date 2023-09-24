

from zooAnimales import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, color_escamas, cantidad_aletas):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.cantidad_aletas = cantidad_aletas
        Pez.listado.append(self)

    @staticmethod
    def cantidad_peces():
        return len(Pez.listado)

    def movimiento(self):
        return "nadar"

    @staticmethod
    def crear_salmon(nombre, edad, genero):
        nuevo_pez = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.salmones += 1
        return nuevo_pez

    @staticmethod
    def crear_bacalao(nombre, edad, genero):
        nuevo_pez = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos += 1
        return nuevo_pez

    def get_cantidad_aletas(self):
        return self.cantidad_aletas

    def set_cantidad_aletas(self, cantidad_aletas):
        self.cantidad_aletas = cantidad_aletas

    def get_color_escamas(self):
        return self.color_escamas

    def set_color_escamas(self, color_escamas):
        self.color_escamas = color_escamas