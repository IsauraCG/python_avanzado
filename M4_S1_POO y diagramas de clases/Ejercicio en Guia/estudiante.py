""" Subclase PROFESOR que hereda de MIEMBRO DE ESCUELA """

#Importa OBJ 'MiembroDeEscuela' del archivo 'miembro_de_escuela'
from miembro_de_escuela import MiembroDeEscuela

class Estudiante(MiembroDeEscuela):
    """ Subclase PROFESOR que hereda de MIEMBRO DE ESCUELA"""
    def __init__(self, nombre, apellido, fecha_nacimiento, sexo, peso, curso, matricula, monto) -> None:
        """ Constructor subclase Profesor """
        super().__init__(nombre,apellido,fecha_nacimiento,sexo,peso)
        self._curso = curso
        self._matricula = matricula
        self._monto = monto

    @property
    def curso(self):
        """ Getter curso Miembro"""
        return self._curso

    @curso.setter
    def curso(self, curso):
        """ Setter curso Miembro """
        self._curso= curso

    @property
    def matricula(self):
        """ Getter matricula Miembro"""
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        """ Setter matricula Miembro """
        self._matricula= matricula

    @property
    def monto(self):
        """ Getter monto Miembro"""
        return self._curso

    @monto.setter
    def monto(self, monto):
        """ Setter monto Miembro """
        self._monto= monto

    def pago_matricula(self):
        """ Método para pago de matrícula
        """
        pago = input(int("Ingrese monto a pagar: "))
        if pago == self.monto:
            print("MATRICULA PAGADA")
        else:
            print("Monto ingresado no coincide con el valor de la matrícula"+
                "\nIntente nuevamente")

    def inscribir_curso(self):
        """Método para inscribir curso a malla del estudiante
        """
        nuevo_curso = input("Ingrese el curso en el que se desea inscribir: ")
        self._curso = nuevo_curso
        print(f"Curso: {self._curso}")