""" Subclase Perro"""

from diseno_clase_animal import Animal

class Perro (Animal):
    """Subclase Perro que deriva de Animal
    Args:
        Animal
    """
    def __init__(self, nombre, raza, edad, peso) -> None:
        """ Constructor de subclase Perro"""
        super().__init__(nombre, raza, edad, peso)


perro = Animal("Brando", "San Bernardo", 3, 30)
Animal.comer(perro,20)
Animal.caminar(perro,3500)
Animal.dormir(perro,9)
