from zooAnimales.animal import Animal

class Mamifero (Animal):
    caballos = 0
    leones = 0
    _cantidadMamiferos = 0
    
    def __init__(self, nombre, edad, habitat, genero,pelaje,patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._cantidadMamiferos  += 1
        

    def isPelaje(self):
        return self._pelaje 
    def getPatas(self):
        return self._patas

    @classmethod
    def cantidadMamiferos(cls):
        return cls._cantidadMamiferos

    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        cls.caballos += 1
        caballo = Mamifero(nombre,edad,"pradera",genero,True,4)
        return caballo

    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        cls.leones += 1
        leon = Mamifero(nombre,edad,"selva",genero,True,4)
        return leon                      


