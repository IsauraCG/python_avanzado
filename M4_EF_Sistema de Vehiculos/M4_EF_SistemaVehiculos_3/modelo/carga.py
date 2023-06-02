""" Clase Automovil de Carga, heredada de Automovil """
from modelo.automovil import Automovil

class Carga(Automovil):
    """ Clase Carga de tipo Automovil que contiene los atributos: 
    (heredados de clase 'Automovil')
        marca, modelo, numero_ruedas, velocidad y cilindrada 
    (propios)
        peso_carga"""

    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, peso_carga):
        # asignación de atributos
        super().__init__(marca, modelo, numero_ruedas,velocidad,cilindrada)
        self._peso_carga= peso_carga

    @property
    def peso_carga(self):
        """ Getter peso_carga"""
        return self._peso_carga

    @peso_carga.setter
    def peso_carga(self, peso_carga):
        """ Setter peso_carga """
        self._peso_carga = peso_carga

    def __str__(self):  # funcion para imprimir el objeto en string, en cualquier tipo de estructura
        """ Método to String """
        string = (
            "Automovil de Carga: " + 
            f"Marca {self._marca}, " + 
            f"Modelo {self._modelo}, " + 
            f"{self._numero_ruedas} ruedas, " + 
            f"Velocidad {self._velocidad} Km/h, " + 
            f"Cilindrada {self._cilindrada} cc, " + 
            f"Carga: {self._peso_carga}Kg.")
        return string
    