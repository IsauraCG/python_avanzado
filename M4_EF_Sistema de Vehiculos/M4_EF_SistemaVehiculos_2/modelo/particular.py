""" Clase Automovil Particular, heredada de Automovil """
from modelo.automovil import Automovil

class Particular(Automovil):
    """ Clase Particular de tipo Automovil que contiene los atributos: 
    (heredados de clase 'Automovil')
        marca, modelo, numero_ruedas, velocidad y cilindrada 
    (propios)
        numeros_puestos"""

    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, numero_puestos):
        # asignación de atributos
        super().__init__(marca, modelo, numero_ruedas,velocidad,cilindrada)
        self._numero_puestos= numero_puestos

    @property
    def numero_puestos(self):
        """ Getter numero_puestos"""
        return self._numero_puestos

    @numero_puestos.setter
    def numero_puestos(self, numero_puestos):
        """ Setter numero_puestos """
        self._numero_puestos = numero_puestos

    def __str__(self):  # funcion para imprimir el objeto en string, en cualquier tipo de estructura
        """ Método to String """
        string = (
            "Nuevo Automovil Particular: " + 
            f"marca={self._marca}, " + 
            f"modelo={self._modelo}, " + 
            f"numero_ruedas={self._numero_ruedas}, " + 
            f"velocidad={self._velocidad}, " + 
            f"cilindrada={self._cilindrada}, " + 
            f"numero_puestos={self._numero_puestos}")
        return string
    