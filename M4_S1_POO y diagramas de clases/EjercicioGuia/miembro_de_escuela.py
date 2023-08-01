""" SUPERCLASE MIEMBRO DE ESCUELA """
from datetime import datetime

class MiembroDeEscuela(object):
    """ Clase MIEMBRO DE ESCUELA """
    def __init__(self, nombre, apellido, fecha_nacimiento, sexo, peso) -> None:
        """ Constructor Clase MIEMBRO DE ESCUELA """
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento
        self._sexo = sexo
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
    def apellido(self):
        """ Getter Apellido Miembro"""
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        """ Setter Apellido Miembro """
        self._apellido= apellido

    @property
    def fecha_nacimiento(self):
        """ Getter Fecha_Nacimiento Miembro"""
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        """ Setter Fecha_Nacimiento Miembro """
        self._fecha_nacimiento= fecha_nacimiento

    @property
    def sexo(self):
        """ Getter sexo Miembro"""
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        """ Setter sexo Miembro """
        self._sexo= sexo

    @property
    def peso(self):
        """ Getter peso Miembro"""
        return self._peso

    @peso.setter
    def peso(self, peso):
        """ Setter peso Miembro """
        self._peso= peso

    def edad (self):
        """ Calcula edad
        """
        anio_actual = int(datetime.today().year)
        anio_nacimiento = int(self.fecha_nacimiento.year)
        miembro_edad = anio_actual - anio_nacimiento
        print (f"{miembro_edad}")

    def imprimir_genero (self):
        """ Imprime texto según sexo
        """
        if self.sexo == "F" :
            print("Femenino")
        elif self.sexo == "M" :
            print("Masculino")
        else : print("ERROR")
