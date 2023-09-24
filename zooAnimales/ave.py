from gestion.zona import Zona
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
    def cantidad_aves():
        return len(Ave.listado)

    def movimiento(self):
        return "Volar"

    @staticmethod
    def crear_halcon(nombre, edad, genero):
        nueva_ave = Ave(nombre, edad, "montañas", genero, "café glorioso")
        Ave.halcones += 1
        return nueva_ave

    @staticmethod
    def crear_aguila(nombre, edad, genero):
        nueva_ave = Ave(nombre, edad, "montañas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        return nueva_ave

    def get_color_plumas(self):
        return self.color_plumas

    def set_color_plumas(self, color_plumas):
        self.color_plumas = color_plumas





