from Modelo.mensajeros import Mensajeros 
from .centroService import CentroService as cs

class MensajeroService:
    def __init__(self):
        self.__lista_mensajeros = []

#--------------------------------------------------------------------------------------------------------------------
    #obtener todos los mensajeros 
    def obtener_mensajeros(self):
        return self.__lista_mensajeros

#--------------------------------------------------------------------------------------------------------------------
    #obtener un mensajero id
    def obtener_mensajero_id(self, id_buscar): 
        for b in self.__lista_mensajeros: 
            if b.id == id_buscar: 
                return b 
        return None 
    
#--------------------------------------------------------------------------------------------------------------------   
    #crear un nuevo mensajero 
    #Como pide que los mensajeros solo tengan dos tipos de estados disponibles y en_transito entonces eso lo indicamos al frontend para que se encargue que solo muestre esa dos opciones al crear el mensajero
    #condiciones (capacidad max no sea menor a 0 y que el centro exista)
    def crear_mensajero(self, mensajero): 
        if isinstance(mensajero, Mensajeros) and mensajero.capacidad > 0: 
            if cs.obtener_centros_id(mensajero.id) and self.existe_mensajero(mensajero.id) != True:
                return mensajero
        return None 
    

    def existe_mensajero(self, existencia_mensajero): 
        for existe in self.__lista_mensajeros: 
            if existe.id == existencia_mensajero: 
                return True
        return False
    #--------------------------------------------------------------------------------------------------------------------

    #cambiar el estado del mensajero: {Un mensajero en Transito no puede ser reasignado a otro centro }

    def cambiar_estado_mensajero(self, id_mensajero, nuevo_estado): 

        if self.existe_mensajero(id_mensajero) == False or nuevo_estado == None: return None 

        mensajero_encontrado = self.obtener_mensajero_id(id_mensajero) #otenemos los mensajeros

        if mensajero_encontrado.estado == "PENDIENTE" and nuevo_estado == "EN_TRANSITO":
            mensajero_encontrado.estado(nuevo_estado) #cambiamos el nuevo estado 
            return mensajero_encontrado
        
        return mensajero_encontrado

    #--------------------------------------------------------------------------------------------------------------------

    #Reasignar Centro: un mensajero en_transito no puede ser reasigando a otro centro
    #Debemos tomar en cuenta: Centro Existente del que queremos reasignar, que el mensajero exista y que el mensajero no este en Transito 

    def reasignar_mensajero_centro(self, id_mensajero, centro_reasignacion): #centro_reasignacion es el ID no un objeto 

        centro_existente = cs.obtener_centros_id(centro_reasignacion)
        mensajero_existente = self.obtener_mensajero_id(id_mensajero)

        if centro_existente == None or mensajero_existente == None: return None 

        if mensajero_existente.centro_asignado == centro_reasignacion or mensajero_existente.estado == "EN_TRANSITO": return mensajero_existente #si no es posible el cambio retornamos el mismo mensajero sin cambios

        #hacemos los cambios 
        mensajero_existente.centro_asignado(centro_reasignacion)

        return mensajero_existente

    #--------------------------------------------------------------------------------------------------------------------

    #Vamos a obtener los mensajeros de cada centro 
    def obtener_mesajeros_centros(self, id_centro): 

        lista_mensajeros_centros = []
        for m in self.__lista_mensajeros: 
            if m.centro_asignado == id_centro: 
                lista_mensajeros_centros.append(m)

        return lista_mensajeros_centros 

    #--------------------------------------------------------------------------------------------------------------------