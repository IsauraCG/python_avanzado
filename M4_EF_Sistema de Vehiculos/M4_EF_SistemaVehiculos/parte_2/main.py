""" Importaciones """
# from modelo.automovil import Automovil
from parte_2.service.automovil_service import AutomovilService

# Test funcion solicitar cantidad
# cantidad = AutomovilService().solicitar_cantidad()

# Test funcion solictar datos
# datos = AutomovilService().solicitar_datos()

# Test de función que imprime los datos de una lista de automoviles en un formato específico
# AutomovilService.imprimir_lista_automoviles(AutomovilService)

######################################

# lista que contendrá los vehículos creados
lista_autos = []
# Función que solicita datos, crea un diccionario con el nuevo vehículo creado
# luego lo añade a la lista recibidas para retornar la lista
automoviles = AutomovilService.crear_automoviles(AutomovilService, lista_autos)
# Función que toma los datos de una lista de automoviles y los imprime en formato solicitados
AutomovilService.imprimir_automoviles_dict(AutomovilService, automoviles)
