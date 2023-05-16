""" Realice los pasos que se detallan a continuación:
1. La clase Libro está definida. 
Cree dos instancias de la clase Libro denominadas libro_1 y libro_2. 
Luego, asigne atributos de instancia a estos objetos (usando la notación de puntos) 
de la siguiente manera:
    ● libro_1:
    ○ autor = 'Dan Brown'
    ○ titulo = 'Infierno'
    ● libro_2:
    ○ autor = 'Dan Brown'
    ○ titulo = 'El Código Da Vinci'
    ○ ann_de_publicacion = 2003
2. En respuesta, imprima el valor del atributo __dict__ de libro_1 y libro_2. 
"""

class Libro:
    """ Clase Libro """
    def __init__ (self, autor = None , titulo = None, publicado = None):
        """ Libro Init """
        self.autor = autor
        self.titulo =titulo
        self.publicado =publicado

    @property
    def autor(self):
        """ property getter """
        return self._autor

    @autor.setter
    def autor (self, autor):
        """ setter """
        self._autor = autor

    @property
    def titulo(self):
        """ property getter """
        return self._titulo

    @titulo.setter
    def titulo(self, autor):
        """ setter """
        self._titulo = autor

    @property
    def publicado(self):
        """ property getter """
        return self._publicado

    @publicado.setter
    def publicado(self, autor):
        """ setter """
        self._publicado = autor

    def __str__(self) -> str:
        """ string """
        return f'Autor:{self._autor}\nTítulo:{self._titulo}\nAño de Publicación:{self._publicado}'

Libro_1 = Libro('Dan Brown','Infierno')
Libro_2 = Libro('Dan Brown','El Código Da Vinci', '2003')

print(Libro_1.__dict__)
#print(Libro_1.__str__)

Libro_1._publicado = '1998'
print(Libro_1.__dict__)
print("=========================================")

print(Libro_2.__dict__)
