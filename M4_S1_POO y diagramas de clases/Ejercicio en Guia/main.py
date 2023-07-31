""" Archivo Main para el manejeo de OBJ
POO = Object Oriented Programming
"""
from datetime import date
from miembro_de_escuela import MiembroDeEscuela
from miembro_de_escuela import edad
from miembro_de_escuela import imprimir_genero

miembro1 = MiembroDeEscuela("Pedro","Cáceres", date(2001,3,20), "F", 45.8)
print(f"{miembro1._nombre, miembro1._apellido,str(miembro1._fecha_nacimiento),miembro1._sexo, miembro1._peso}")
edad(miembro1)
imprimir_genero(miembro1)