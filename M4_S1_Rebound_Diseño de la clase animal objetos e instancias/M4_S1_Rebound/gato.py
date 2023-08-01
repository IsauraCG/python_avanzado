""" Subclase Perro"""

from diseno_clase_animal import Animal

class Gato (Animal):
    """Subclase Perro que deriva de Animal
    Args:
        Animal
    """
    def __init__(self, nombre, raza, edad, peso) -> None:
        """ Constructor de subclase Perro"""
        super().__init__(nombre, raza, edad, peso)


gato = Animal("Roll", "Persa", 4, 3)
Animal.comer(gato,20)
Animal.caminar(gato,750)
Animal.dormir(gato,10)
