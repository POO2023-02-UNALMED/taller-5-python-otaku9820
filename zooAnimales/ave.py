
from zooAnimales.animal import Animal 

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, color_plumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = color_plumas
        Ave._listado.append(self)

    @staticmethod
    def cantidadAves():
        return len(Ave._listado)

    def movimiento(self):
        return "Volar"

    @classmethod
    def crearHalcon(cls,nombre, edad, genero):
        nueva_ave = cls(nombre, edad, "montañas", genero, "café glorioso")
        Ave.halcones += 1
        return nueva_ave

    @classmethod
    def crearAguila(cls,nombre, edad, genero):
        nueva_ave = cls(nombre, edad, "montañas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        return nueva_ave

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, color_plumas):
        self._colorPlumas = color_plumas
        
    def toString(self):
        return "mi nombre es ",self._nombre, ", tengo una edad de", self._edad, ", habito en", self._habitat, " y mi genero es", self._genero





