from mensajeros import Mensajeros

class Paquetes: 
    def __init__(self, id, peso, centro_origen, centro_destino, estado, cliente):
        self.__id = id 
        self.__peso = peso 
        self.__centro_origen = centro_origen
        self.__centro_destino = centro_destino
        self.__estado = estado 
        self.__cliente = cliente 
        self.__mensajero_asignado = None 

    @property
    def id(self):
        return self.__id
    
    @property
    def peso(self):
        return self.__peso 
    
    @property
    def centro_origen(self):
        return self.__centro_origen
    
    @property
    def centro_destino(self):
        return self.__centro_destino 
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def cliente(self):
        return self.__cliente

    @property
    def mensajero_asignado(self):
        return self.__mensajero_asignado
    
    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id 

    @peso.setter
    def peso(self, nuevo_peso):
        if nuevo_peso > 0:
          self.__peso = nuevo_peso


    @centro_origen.setter
    def centro_origen(self, nuevo_centro_origen):
        self.__centro_origen = nuevo_centro_origen 

    @centro_destino.setter
    def centro_destino(self, nuevo_centro_destino):
        self.__centro_destino =nuevo_centro_destino

    @estado.setter
    def estado(self, nuevo_estado):
        self.__estado = nuevo_estado
        
    @cliente.setter
    def cliente(self, nuevo_cliente):
        self.__cliente = nuevo_cliente 
    
    @mensajero_asignado.setter
    def mensajero_asignado(self, nuevo_mensajero):
        if isinstance(nuevo_mensajero, Mensajeros): #isintance verifica si un objeto le pertenece a una clase isinstance(obj, Clase) devuelve:  True → si obj es de esa clase False → si no lo es
            self.__mensajero_asignado = nuevo_mensajero

 