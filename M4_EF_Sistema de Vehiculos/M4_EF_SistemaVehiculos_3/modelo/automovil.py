""" Clase Automóvil, heredada de Vehículo """
from modelo.vehiculo import Vehiculo


class Automovil(Vehiculo):
    """ Clase automovil que contiene atributos: 
    (heredados de clase 'Vehiculo')
        marca, modelo y numero_ruedas ,
    (propios)
    velocidad y cilindrada """

    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):
        # asignación de atributos
        super().__init__(marca, modelo, numero_ruedas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada

    @property
    def velocidad(self):
        """ Getter velocidad"""
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        """ Setter velocidad """
        self._velocidad = velocidad

    @property
    def cilindrada(self):
        """ Getter cilindrada"""
        return self._cilindrada

    @cilindrada.setter
    def cilindrada(self, cilindrada):
        """ Setter cilindrada """
        self._cilindrada = cilindrada

    def __str__(self):  # funcion para imprimir el objeto en string, en cualquier tipo de estructura
        # return super().__str__()
        """ Método to String """
        string = (
            "Nuevo Automovil: " + 
            f"marca={self._marca}, " + 
            f"modelo={self._modelo}, " + 
            f"numero_ruedas={self._numero_ruedas}, " + 
            f"velocidad={self._velocidad}, " + 
            f"cilindrada={self._cilindrada}")
        return string
