""" Clase Bicicleta, heredada de Vehículo """
from modelo.vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    """ Clase Bicicleta de tipo Vehículo que contiene los atributos: 
    (heredados de clase 'Vehiculo')
        marca, modelo y numero_ruedas
    (propios)
        tipo_bicicleta"""

    def __init__(self, marca, modelo, numero_ruedas, tipo_bicicleta):
        # asignación de atributos
        super().__init__(marca, modelo, numero_ruedas)
        self._tipo_bicicleta= tipo_bicicleta

    @property
    def tipo_bicicleta(self):
        """ Getter tipo_bicicleta"""
        return self._tipo_bicicleta

    @tipo_bicicleta.setter
    def tipo_bicicleta(self, tipo_bicicleta):
        """ Setter tipo_bicicleta """
        self._tipo_bicicleta = tipo_bicicleta

    def __str__(self):  # funcion para imprimir el objeto en string, en cualquier tipo de estructura
        """ Método to String """
        string = (
            "Bicicleta: " + 
            f"Marca {self._marca}, " + 
            f"Modelo {self._modelo}, " + 
            f"{self._numero_ruedas} ruedas, " + 
            f"Tipo: {self._tipo_bicicleta}")
        return string
    