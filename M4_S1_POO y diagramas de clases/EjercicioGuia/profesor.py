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
    def curso(self):
        """ Getter curso Miembro"""
        return self._curso

    @curso.setter
    def curso(self, curso):
        """ Setter curso Miembro """
        self._curso= curso

    @property
    def salario(self):
        """ Getter salario Miembro"""
        return self._salario

    @salario.setter
    def salario(self, salario):
        """ Setter salario Miembro """
        self._salario= salario

    def curso_impartiendo(self):
        """ Función cuaro impartiendo """
        print(f"Impartiendo el curso: {self.curso} ")

    def salario_anual(self):
        """ Método salario anual """
        salario_mensual = int(self.salario)
        print(f"Salario Anual: {salario_mensual*12}")
