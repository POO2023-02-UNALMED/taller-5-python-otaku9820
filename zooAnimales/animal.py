
import zooAnimales


class Animal:
    _total_animales = 0
    _zona=""

    def __init__(self, nombre, edad, habitat, genero):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        
        Animal.total_animales += 1
        

    def movimiento(self):
        return "Desplazarse"

    @staticmethod
    def total_por_tipo():
        resultado = (
            f"Mamíferos: {zooAnimales.mamifero.Mamiferos.cantidad_mamiferos()}, "
            f"Aves: {zooAnimales.ave.Ave.cantidad_aves()}, "
            f"Reptiles: {zooAnimales.reptil.Reptil.cantidad_reptiles()}, "
            f"Peces: {zooAnimales.pez.Pez.cantidad_peces()}, "
            f"Anfibios: {zooAnimales.anfibio.Anfibio.cantidad_anfibios()}"
        )
        return resultado

    def __str__(self):
        return (
            f"Mi nombre es {self.nombre}, "
            f"Tengo una edad de {self.edad}, "
            f"habito en {self.habitat}, "
            f"y mi genero es {self.genero}, "
            f"la zona en la que me ubico es {self.zona}"
        )

    @classmethod
    def getTotalAnimales(cls):
        return cls.total_animales

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getHabitat(self):
        return self.habitat

    def getGenero(self):
        return self.genero

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setHabitat(self, habitat):
        self.habitat = habitat

    def setGenero(self, genero):
        self.genero = genero