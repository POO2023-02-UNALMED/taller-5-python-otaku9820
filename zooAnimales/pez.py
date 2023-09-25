

from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, color_escamas, cantidad_aletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = color_escamas
        self._cantidadAletas = cantidad_aletas
        Pez._listado.append(self)

    @staticmethod
    def cantidadPeces():
        return len(Pez._listado)

    def movimiento(self):
        return "nadar"

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        nuevo_pez = cls(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.salmones += 1
        return nuevo_pez

    @classmethod
    def crearBacalao(cls,nombre, edad, genero):
        nuevo_pez = cls(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos += 1
        return nuevo_pez

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidad_aletas):
        self._cantidadAletas = cantidad_aletas

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, color_escamas):
        self._colorEscamas = color_escamas