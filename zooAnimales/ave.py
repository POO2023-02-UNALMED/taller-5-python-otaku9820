
from zooAnimales.animal import Animal 

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, color_plumas):
        super().__init__(nombre, edad, habitat, genero)
        self.color_plumas = color_plumas
        Ave.listado.append(self)

    @staticmethod
    def cantidadAves():
        return len(Ave.listado)

    def movimiento(self):
        return "Volar"

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        nueva_ave = Ave(nombre, edad, "montañas", genero, "café glorioso")
        Ave.halcones += 1
        return nueva_ave

    @staticmethod
    def crearAguila(nombre, edad, genero):
        nueva_ave = Ave(nombre, edad, "montañas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        return nueva_ave

    def getcolorPlumas(self):
        return self.color_plumas

    def setColorPlumas(self, color_plumas):
        self.color_plumas = color_plumas





