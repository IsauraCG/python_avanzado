""" Super Clase PERSONA """
class Persona:
    """ Clase PERSONA """
    def __init__(self, nombre) -> None:
        """ Constructor Clase Persona """
        self._nombre = nombre

    @property
    def nombre(self):
        """ Getter Nombre Persona"""
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        """ Setter Nombre Persona """
        self._nombre= nombre

    def movimiento(self, accion):
        """ Método Movimiento. Args (self,accion) """
        print(f'{self._nombre} = {accion}')
