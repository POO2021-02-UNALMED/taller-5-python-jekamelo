class Zoologico:

    def __init__(self,nombre,ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarZonas(self,zona):
        self._zonas.append(zona)

    @classmethod
    def cantidadTotalAnimales(cls):
        pass

    def getNombre(self):
        return self._nombre

    def getUbicacion(self):
        return self._ubicacion    
