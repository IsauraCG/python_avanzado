from persona import Persona


class Cliente(Persona):
    def __init__(self, nombre, apellido, rut, descuento):
        # invocando a los atributos de la super clase Persona
        Persona.__init__(nombre, apellido, rut)
        self._descuento = descuento  # atributo agregado para Cliente

    @property
    def descuento(self):
        return self._descuento

    @descuento.setter
    def descuento(self, descuento):
        self._descuento = descuento

    def __str__(self):
        # return super().__str__()
        return f'Cliente(nombre={self._nombre}, apellido={self._apellido}, rut={self._rut}, descuento={self._descuento})'
