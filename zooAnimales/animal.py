
import zooAnimales


class Animal:
    _total_animales = 0
    _zona=""

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        
        Animal._total_animales += 1
        

    def movimiento(self):
        return "Desplazarse"

    @staticmethod
    def totalPorTipo():
        resultado = (
            f"Mamíferos: {zooAnimales.mamifero.Mamifero.cantidad_mamiferos()}, "
            f"Aves: {zooAnimales.ave.Ave.cantidad_aves()}, "
            f"Reptiles: {zooAnimales.reptil.Reptil.cantidad_reptiles()}, "
            f"Peces: {zooAnimales.pez.Pez.cantidad_peces()}, "
            f"Anfibios: {zooAnimales.anfibio.Anfibio.cantidad_anfibios()}"
        )
        return resultado

    def __str__(self):
        return (
            f"Mi nombre es {self._nombre}, "
            f"Tengo una edad de {self._edad}, "
            f"habito en {self._habitat}, "
            f"y mi genero es {self._genero}, "
            f"la zona en la que me ubico es {self._zona}"
        )

    @classmethod
    def getTotalAnimales(cls):
        return cls.total_animales

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setHabitat(self, habitat):
        self.habitat = habitat

    def setGenero(self, genero):
        self.genero = genero