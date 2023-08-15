class Persona:
    def __init__(self, nombre, apellido, anio):
        self._nombre = nombre
        self._apellido = apellido
        self._anio = anio

    @property
    def nombre(self):
        """ Getter Nombre Persona"""
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        """ Setter Nombre Persona """
        self._nombre = nombre

    @property
    def apellido(self):
        """ Getter Apellido Persona"""
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        """ Setter Apellido Persona """
        self._apellido = apellido

    @property
    def anio(self):
        """ Getter Anio Persona"""
        return self._anio

    @anio.setter
    def anio(self, anio):
        """ Setter Anio Persona """
        self._anio = anio
