from zooAnimales.animal import Animal

class Pez (Animal):
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero,colorEscamas,cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    def getColorEscamas(self):
        return self._colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas

    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        cls.salmones += 1
        salmon = Pez(nombre,edad,"oceano",genero,"rojo",6)
        return salmon

    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        cls.bacalaos += 1
        bacalao = Pez(nombre,edad,"oceano",genero,"gris",6)
        return bacalao
                