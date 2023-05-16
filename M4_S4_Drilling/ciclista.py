""" Subclase Ciclista que hereda de Persona """

#Importa OBJ 'Persona' del archivo 'persona'
from persona import Persona

class Ciclista(Persona):
    """ Subclase Ciclista """
    def __init__(self,nombre) -> None:
        """ Constructor """
        super().__init__(nombre)

#   ==============================
# FORMA PARA ELIMINAR Pylint warning for "useless super delegation"
#   NOTA: YA QUE  DE NO TENER OTRO ATRIBUTO, SÓLO REPITE EL CÓDIGO DE OBJ PERSONA

# class Ciclista(Persona):
#     def __init__(self,nombre,cadencia) -> None:
#         super().__init__(nombre)
#         self._cadencia = cadencia
#   ==============================

# OTRA FORMA PARA ELIMINAR Pylint warning for "useless super delegation"
#   NOTA: AL USAR 'pass' ESTAMOS LLAMANDO AL MÉTODO DE LA SUPERCLASS OBJ PERSONA

# class Ciclista(Persona):
#     pass
