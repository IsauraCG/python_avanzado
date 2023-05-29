class Departamento:
    def __init__(self, nombre_depto, nombre_corto_depto):
        self._nombre_depto = nombre_depto
        self._nombre_corto_depto = nombre_corto_depto

    @property
    def nombre_depto(self):
        """ Getter nombre_depto Departamento"""
        return self._nombre_depto

    @nombre_depto.setter
    def nombre_depto(self, nombre_depto):
        """ Setter nombre_depto Departamento """
        self._nombre_depto = nombre_depto

    @property
    def nombre_corto_depto(self):
        """ Getter nombre_corto_depto Departamento"""
        return self._nombre_corto_depto

    @nombre_corto_depto.setter
    def nombre_corto_depto(self, nombre_corto_depto):
        """ Setter nombre_corto_depto Departamento """
        self._nombre_corto_depto = nombre_corto_depto
