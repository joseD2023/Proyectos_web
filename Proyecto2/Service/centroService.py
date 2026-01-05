
from Modelo.centros import Centros

class CentroService:
    def __init__(self):
        self.__lista_centros = []


    #obtener centros 
    def obtener_centros(self): 
        return self.__lista_centros
    
    
    #obtener centros por id 
    def obtener_centros_id(self, id_buscar):
        for b in self.__lista_centros: 
            if b.id == id_buscar: 
                return b 
        return None

            
    #crear un nuevo centro --------------------------------------------------------------------------------------------      
    def crear_centro_nuevo(self, centro_nuevo):
        if isinstance(centro_nuevo, Centros) and centro_nuevo.capacidad > 0: #si pertenece a la clase puede crearses
            if self.existe_centro_id(centro_nuevo.id) != True:
             self.__lista_centros.append(centro_nuevo)
             return centro_nuevo
        return None
    

    
    def existe_centro_id(self, centro_verificar): 
        for v in self.__lista_centros: 
            if v.id == centro_verificar: 
                return True
        return False
    






    
    