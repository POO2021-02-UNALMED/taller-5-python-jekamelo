
class Animal:
    totalAnimales = 0
    def __init__(self,nombre,edad,habitat,genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = []
        Animal.totalAnimales +=1

    def getNombre(self):
        return  self._nombre
    def getEdad(self):
        return  self._edad
    def getHabitat(self):
        return  self._habitat
    def getGenero(self):
        return  self._genero

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil

        mamifero = "Mamiferos :"+" "+str(Mamifero.cantidadMamiferos())
        reptil = "Reptiles :"+" "+str(Reptil.cantidadReptiles())
        ave = "Aves :"+" "+str(Ave.cantidadAves())
        anfibio = "Anfibios :"+" "+str(Anfibio.cantidadAnfibios())
        pez = "Peces :"+" "+str(Pez.cantidadPeces())
        return mamifero+ave+reptil+pez+anfibio

        

    def toString(self):
        return "Mi nombre es "+self._nombre+", tengo una edad de "+str(self._edad)+", habito en "+self._habitat+" y mi genero es "+self._genero

        