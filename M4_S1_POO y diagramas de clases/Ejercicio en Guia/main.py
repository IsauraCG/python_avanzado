""" Archivo Main para el manejeo de OBJ
POO = Object Oriented Programming
"""
from datetime import date
from miembro_de_escuela import MiembroDeEscuela
from miembro_de_escuela import edad
from miembro_de_escuela import imprimir_genero
from profesor import Profesor
from profesor import curso_impartiendo
from profesor import salario_anual
from estudiante import Estudiante
from estudiante import pago_matricula
from estudiante import inscribir_curso

miembro1 = MiembroDeEscuela("Pedro","Cáceres", date(2001,3,20), "M", 45.8)
print(f"{miembro1.nombre, miembro1.apellido,str(miembro1.fecha_nacimiento),miembro1.sexo, miembro1.peso}")
edad(miembro1)
imprimir_genero(miembro1)

estudiante1 = Estudiante("Juan","Robledo", date(2017,4,13),"M",20, "4to-A", "PENDIENTE", 120000)
pago_matricula(estudiante1)
inscribir_curso(estudiante1)
