
class Mensajeros:
    def __init__(self, id, nombre, capacidad_max, centro_asignado):
        self.__id = id 
        self.__nombre = nombre 
        self.__capacidad = capacidad_max
        self.__centro_asignado = centro_asignado
        self.__estado = "PENDIENTE"
        self.__cantidad_paquetes = 0
    
    @property
    def id(self):
        return self.__id 

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def capacidad(self):
        return self.__capacidad
    
    @property
    def centro_asignado(self):
        return self.__centro_asignado
    
    @property
    def estado(self):
        return self.__estado 
    
    @property
    def cantidad_paquetes(self):
        return self.__cantidad_paquetes
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    @capacidad.setter
    def capacidad(self, nueva_capacidad):
        self.__capacidad = nueva_capacidad

    @centro_asignado.setter
    def centro_asignado(self, nuevo_centro_asignado):
        self.__centro_asignado = nuevo_centro_asignado


    @estado.setter
    def estado(self, nuevo_estado):
        if nuevo_estado == "PENDIENTE" or nuevo_estado == "EN_TRANSITO":
            self.__estado = nuevo_estado
            

    def agregar_paquetes(self):
        self.__cantidad_paquetes += 1 

    def quitar_paquetes(self):
        self.__cantidad_paquetes -= 1

        
