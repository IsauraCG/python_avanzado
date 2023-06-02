""" Clase Vehículo """


class Vehiculo:
    """ Clase vehículo que contiene: marca, modelo y numero_ruedas"""

    def __init__(self, marca, modelo, numero_ruedas):
        # asignación de atributos
        self._marca = marca
        self._modelo = modelo
        self._numero_ruedas = numero_ruedas

    @property
    def marca(self):
        """ Getter Marca"""
        return self._marca

    @marca.setter
    def marca(self, marca):
        """ Setter Marca """
        self._marca = marca

    @property
    def modelo(self):
        """ Getter Modelo"""
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        """ Setter Modelo """
        self._modelo = modelo

    @property
    def numero_ruedas(self):
        """ Getter Numero de Ruedas"""
        return self._numero_ruedas

    @numero_ruedas.setter
    def numero_ruedas(self, numero_ruedas):
        """ Setter Numero de Ruedas """
        self._numero_ruedas = numero_ruedas
