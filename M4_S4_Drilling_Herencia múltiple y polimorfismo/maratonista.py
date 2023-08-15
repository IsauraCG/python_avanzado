""" Subclase Maratonista que hereda de Persona """
# Importa OBJ 'Persona' de archivo 'persona'
from persona import Persona

class Maratonista(Persona):
    """ Subclase Maratonista """
    def __init__(self, nombre) -> None:
        """ Maratonista Constructor """
        super().__init__(nombre)
