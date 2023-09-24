

from zooAnimales.animal import Animal

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
    def cantidadPeces():
        return len(Pez.listado)

    def movimiento(self):
        return "nadar"

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        nuevo_pez = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.salmones += 1
        return nuevo_pez

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        nuevo_pez = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos += 1
        return nuevo_pez

    def getCantidad_aletas(self):
        return self.cantidad_aletas

    def setCantidad_aletas(self, cantidad_aletas):
        self.cantidad_aletas = cantidad_aletas

    def getColorEscamas(self):
        return self.color_escamas

    def setColorEscamas(self, color_escamas):
        self.color_escamas = color_escamas