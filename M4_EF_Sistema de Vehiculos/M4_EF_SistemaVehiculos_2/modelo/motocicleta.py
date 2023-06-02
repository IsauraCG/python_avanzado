""" Clase Motocicleta, heredada de Bicicleta """
from modelo.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    """ Clase Motocicleta de tipo Bicicleta, y que contiene los atributos: 
    (heredados de clase 'Bicicleta')
        marca, modelo, numero_ruedas y tipo_bicicleta
    (propios)
        nro_radios, cuadro y motor """

    def __init__(self, marca, modelo, numero_ruedas, tipo_bicicleta, nro_radios, cuadro, motor):
        # asignación de atributos
        super().__init__(marca, modelo, numero_ruedas, tipo_bicicleta)
        self._nro_radios= nro_radios
        self._cuadro= cuadro
        self._motor= motor

    @property
    def nro_radios(self):
        """ Getter nro_radios"""
        return self._nro_radios

    @nro_radios.setter
    def nro_radios(self, nro_radios):
        """ Setter nro_radios """
        self._nro_radios = nro_radios
        
    @property
    def cuadro(self):
        """ Getter cuadro"""
        return self._cuadro

    @cuadro.setter
    def cuadro(self, cuadro):
        """ Setter cuadro """
        self._cuadro = cuadro
        
    @property
    def motor(self):
        """ Getter motor"""
        return self._motor

    @motor.setter
    def motor(self, motor):
        """ Setter motor """
        self._motor = motor

    def __str__(self):  # funcion para imprimir el objeto en string, en cualquier tipo de estructura
        """ Método to String """
        string = (
            "Nuevo Automovil Particular: " + 
            f"marca={self._marca}, " + 
            f"modelo={self._modelo}, " + 
            f"numero_ruedas={self._numero_ruedas}, " + 
            f"tipo_bicicleta={self._tipo_bicicleta}, " +
            f"nro_radios={self._nro_radios}" + 
            f"cuadro={self._cuadro}, " +
            f"motor={self._motor}, ")
        return string
    