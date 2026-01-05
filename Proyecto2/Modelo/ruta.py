
class Ruta:
    def __init__(self, id, centro_origen, centro_destino, distancia):
        self.__id = id 
        self.__centro_origen = centro_origen
        self.__centro_destino = centro_destino
        self.__distancia = distancia 

    @property
    def id(self):
        return self.__id
    
    @property
    def centro_origen(self):
        return self.__centro_origen
    
    @property
    def centro_destino(self):
        return self.__centro_destino
    
    @property
    def distancia(self):
        return self.__distancia
    
    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id
    
    @centro_origen.setter
    def centro_origen(self, nuevo_centro_origen):
        self.centro_origen = nuevo_centro_origen
    
    @centro_destino.setter
    def centro_destino(self, nuevo_centro_destino):
        self.centro_destino = nuevo_centro_destino

    @distancia.setter
    def distancia(self, nueva_distancia):
        self.__distancia = nueva_distancia