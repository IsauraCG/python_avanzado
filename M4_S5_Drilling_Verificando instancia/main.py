""" Construya las siguientes clases, con los siguientes atributos:
● Persona
    - nombre
    - apellido
    - anio
● Departamento
    - nombre_dpto
    - nombre_corto_dpto
● Trabajador (Persona, Departamento)
    - nombre
    - apellido
    - anio
    - nombre_dpto
    - nombre_corto_dpto
    - salario
Construya el objeto trabajador con los siguientes datos:
    - nombre: Juan
    - apellido:Pérez
    - anio: 2005
    - nombre_dpto: Ingeniería de software
    - nombre_corto_dpto: IS
    - salario: 20000 """

from persona import Persona
from departamento import Departamento
from trabajador import Trabajador

if __name__ == '__main__':
    trabajador = Trabajador('Juan', 'Perez', 2005,
                            'Ingenieria de Software', 'IS')
    trabajador.salario = 20_000
    print(trabajador.__dict__)
    # la instancia de clase Trabajador
    print("Es trabajador instancia de Persona: " +
          isinstance(trabajador, Persona))
    print("Es trabajador instancia de Persona: " +
          isinstance(trabajador, Departamento))
    print("Es trabajador instancia de Persona: " +
          isinstance(trabajador, Trabajador))
