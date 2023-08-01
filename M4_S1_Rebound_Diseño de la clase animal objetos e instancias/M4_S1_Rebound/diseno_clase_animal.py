""" Superclase Animal"""

class Animal(object):
    """ Clase Animal"""
    def __init__(self, nombre, raza, edad, peso) -> None:
        """ constructor de clase animal"""
        self._nombre = nombre
        self._raza = raza
        self._edad = edad
        self._peso = peso

    @property
    def nombre(self):
        """ Getter Nombre Miembro"""
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        """ Setter Nombre Miembro """
        self._nombre= nombre

    @property
    def raza(self):
        """ Getter raza Miembro"""
        return self._raza

    @raza.setter
    def raza(self, raza):
        """ Setter raza Miembro """
        self._raza= raza

    @property
    def edad(self):
        """ Getter edad Miembro"""
        return self._edad

    @edad.setter
    def edad(self, edad):
        """ Setter edad Miembro """
        self._edad= edad

    @property
    def peso(self):
        """ Getter peso Miembro"""
        return self._peso

    @peso.setter
    def peso(self, peso):
        """ Setter peso Miembro """
        self._peso= peso
