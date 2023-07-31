""" Subclase PROFESOR que hereda de MIEMBRO DE ESCUELA """

#Importa OBJ 'MiembroDeEscuela' del archivo 'miembro_de_escuela'
from miembro_de_escuela import MiembroDeEscuela

class Profesor(MiembroDeEscuela):
    """ Subclase PROFESOR que hereda de MIEMBRO DE ESCUELA"""
    def __init__(self, nombre, apellido, fecha_nacimiento, sexo, peso, curso, salario) -> None:
        """ Constructor subclase Profesor """
        super().__init__(nombre,apellido,fecha_nacimiento,sexo,peso)
        self._curso = curso
        self._salario = salario

    @property
    def nombre(self):
        """ Getter Nombre Miembro"""
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        """ Setter Nombre Miembro """
        self._nombre= nombre
        