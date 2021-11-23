from zooAnimales.animal import Animal

class Reptil (Animal):
    serpientes = 0
    iguanas = 0


    def __init__(self, nombre, edad, habitat, genero,colorEscamas,largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

    def getColorEscamas(self):
        return self._colorEscamas
    def getLargoCola(self):
        return self._largoCola

    @classmethod
    def crearSerpiente(cls,nombre,edad,genero):
        cls.serpientes += 1
        serpiente = Reptil(nombre,edad,"jungla",genero,"blanco",1)
        return serpiente

    @classmethod
    def crearIguana(cls,nombre,edad,genero):
        cls.iguanas += 1
        iguana = Reptil(nombre,edad,"jungla",genero,"verde",3)        
        return iguana        