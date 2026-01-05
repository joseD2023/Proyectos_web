class Solicitud:
    def __init__(self, id, id_paquete, tipo, prioridad):
        self.__id = id 
        self.__id_paquete = id_paquete
        self.__tipo = tipo 
        self.__prioridad = prioridad
        self.__estado = "PENDIENTE"

    @property
    def id(self):
        return self.__id
    
    @property
    def id_paquete(self):
        return self.__id_paquete
    
    @property
    def tipo(self):
        return self.__tipo 
    
    @property
    def prioridad(self):
        return self.__prioridad
    
    @property
    def estado(self):
        return self.__estado
    
    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    @id_paquete.setter
    def id_paquete(self, nuevo_paquete):
        self.__id_paquete = nuevo_paquete

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self.__tipo = nuevo_tipo

    @prioridad.setter
    def prioridad(self, nueva_prioridad):
        if nueva_prioridad > 0: 
            self.__prioridad = nueva_prioridad

    @estado.setter
    def estado(self, nuevo_estado):
        self.__estado = nuevo_estado


    
