#vamos a definir nuestras clases como detalle de datos 

class Centros:
    def __init__(self, id, nombre, ubicacion, capacidad):
        self.__id = id 
        self.__nombre = nombre 
        self.__ubicacion = ubicacion 
        self.__capacidad = capacidad
        self.__paquetes = 0

    def __repr__(self):
        
        return f"""
    ID Centro: {self.__id}
    Nombre Centro: {self.__nombre}
    Ubicacion Centro: {self.__ubicacion}
    Capacidad Centro: {self.__capacidad}
    Paquetes Centro: {self.__paquetes}
"""

    def __str__(self):

        return f"""
    ID Centro: {self.__id}
    Nombre Centro: {self.__nombre}
    Ubicacion Centro: {self.__ubicacion}
    Capacidad Centro: {self.__capacidad}
    Paquetes Centro: {self.__paquetes}
"""

    #ahora vamos hacer getters  y setters 
    @property
    def id(self):
        return self.__id

    @property 
    def nombre(self):
        return self.__nombre
    
    @property
    def ubicacion(self):
        return self.__ubicacion
    
    @property
    def capacidad(self):
        return self.__capacidad
    
    @property
    def paquetes(self): 
        return self.__paquetes
    
    @id.setter
    def id(self, id_nuevo):
        self.__id = id_nuevo
    
    @nombre.setter 
    def nombre(self, nombre_nuevo):
        self.__nombre = nombre_nuevo

    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion):
        self.__ubicacion = nueva_ubicacion

    @capacidad.setter
    def capacidad(self, nueva_capacidad):
        if nueva_capacidad > 0: 
            self.__capacidad = nueva_capacidad

    #Metodos para la accion del centro 
    def agregar_paquetes(self):
        self.__paquetes += 1 
  

    def quitar_paquetes(self):
        if self.__paquetes > 0:
            self.__paquetes -= 1 

    def mostrar_informacion(self): 
        return None



        