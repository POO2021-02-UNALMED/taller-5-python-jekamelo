from zooAnimales.animal import Animal


class Anfibio (Animal):
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero,colorPiel,venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

    def isVenenoso(self):
        return self._venenoso

    def getColorPiel(self):
        return self._colorPiel

    @classmethod
    def crearRana(cls,nombre,edad,genero):
        cls.ranas += 1
        rana = Anfibio(nombre,edad,"selva",genero,"rojo",True)
        return rana

    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        cls.salamandras += 1
        salamandra = Anfibio(nombre,edad,"selva",genero,"rojo",True)
        return salamandra        

                