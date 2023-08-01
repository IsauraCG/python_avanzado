""" Archivo Main para el manejeo de OBJ
POO = Object Oriented Programming
"""
from datetime import date
from miembro_de_escuela import MiembroDeEscuela
from profesor import Profesor
from estudiante import Estudiante

miembro1 = MiembroDeEscuela("Pedro","Cáceres", date(2001,3,20), "M", 45.8)
print(f"{miembro1.nombre, miembro1.apellido,str(miembro1.fecha_nacimiento),miembro1.sexo, miembro1.peso}")
MiembroDeEscuela.edad(miembro1)
MiembroDeEscuela.imprimir_genero(miembro1)

profesor1 = Profesor("Luis", "López",date(1986,1,20),"M",58.3,"3ro-A",350000)
Profesor.curso_impartiendo(profesor1)
Profesor.salario_anual(profesor1)

estudiante1 = Estudiante("Juan","Robledo", date(2017,4,13),"M",20, "4to-A", "PENDIENTE", 120000)
Estudiante.pago_matricula(estudiante1)
Estudiante.inscribir_curso(estudiante1)
