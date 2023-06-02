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
            "Automovil Particular: " + 
            f"Marca {self._marca}, " + 
            f"Modelo {self._modelo}, " + 
            f"{self._numero_ruedas} ruedas, " + 
            f"Velocidad {self._velocidad} Km/h, " + 
            f"Cilindrada {self._cilindrada} cc, " + 
            f"Puestos: {self._numero_puestos}")
        return string
    