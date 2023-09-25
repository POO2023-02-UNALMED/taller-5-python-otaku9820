
from gestion.zona import Zona



class Zoologico:
    _zonas=[]
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        

    def cantidadTotalAnimales(self):
        x=0
        for i in self._zonas:
            x+=i.cantidadAnimales()
            
        return x

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre
        
        
    @classmethod
    def getZona(cls):
        return cls._zonas
    @classmethod
    def setZona(cls, zona):
        cls._zonas = zona