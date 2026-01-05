from Modelo.centros import Centros
from Service.centroService import CentroService



c = CentroService()

centro_nuevo = Centros("C001", "Centro Azure", "Guatemala", 500)
centro_nuevo1 = Centros("C002", "Centro aws", "Guatemala", 600)
centro_nuevo2= Centros("C003", "Centro Cloud", "Guatemala", 900)
centro_nuevo3 = Centros("C004", "Centro gt", "Guatemala", 700)

print(c.crear_centro_nuevo(centro_nuevo))
print(c.crear_centro_nuevo(centro_nuevo1))
print(c.crear_centro_nuevo(centro_nuevo2))
print(c.crear_centro_nuevo(centro_nuevo3))


#ahora le damos a buscar algun centro para verificar si realmente existe 

print(c.obtener_centros())

print("AHORA VAMOS A BUSCAR UN CENTRO DE ID PARA VERFICAR SI SIRVE LA BUSQEUDA VAMOS A BUSCAR C004")

print(c.obtener_centros_id("C004"))