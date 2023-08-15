""" Main: importa los objetos, las clases y trabaja con sus métodos """
from persona import Persona
from ciclista import Ciclista
from maratonista import Maratonista

persona_1 = Persona('La Persona')
persona_1.movimiento('Caminando')

ciclista_1 = Ciclista('El Ciclista')
ciclista_1.movimiento('Rodando')

maratonista_1 = Maratonista('El Maratonista')
maratonista_1.movimiento('Trotando')
