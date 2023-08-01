""" Superclase Animal"""

class Animal(object):
    """ Clase Animal"""
    def __init__(self, nombre, raza, edad, peso) -> None:
        """ constructor de clase animal"""
        self._nombre = nombre
        self._raza = raza
        self._edad = edad
        self._peso = peso

    @property
    def nombre(self):
        """ Getter Nombre Miembro"""
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        """ Setter Nombre Miembro """
        self._nombre= nombre

    @property
    def raza(self):
        """ Getter raza Miembro"""
        return self._raza

    @raza.setter
    def raza(self, raza):
        """ Setter raza Miembro """
        self._raza= raza

    @property
    def edad(self):
        """ Getter edad Miembro"""
        return self._edad

    @edad.setter
    def edad(self, edad):
        """ Setter edad Miembro """
        self._edad= edad

    @property
    def peso(self):
        """ Getter peso Miembro"""
        return self._peso

    @peso.setter
    def peso(self, peso):
        """ Setter peso Miembro """
        self._peso= peso

    # Métodos:  comer, caminar, dormir

    def comer(self, cant_comida):
        """ Método: comer del OBJ animal 
        cant_comida : expresada en gramos """
        print (f"{self._nombre} ha comido {cant_comida} gramos de comida")
        # convierte en gramos el peso, y le suma cant_comida
        self._peso = (self._peso * 1000) + cant_comida
        # reconvierte a kilogramos
        self._peso = self._peso / 1000
        #imprime mensaje en consola
        print (f"El nuevo peso de {self._nombre} es: {self._peso} kgs.")

    def caminar(self, cant_pasos):
        """ Método: caminar del OBJ animal """
        # 257.143 pasos == 1000 grs
        # 1 paso == 0,0039 grs

        #cálculo de correspondencia del peso perdido, según cantidad de pasos ingresada
        peso_perdido = int(cant_pasos * 0.0039)
        # actualizar valor del peso, segun peso perdido
        self._peso = float(((self._peso * 1000) - peso_perdido)/1000)
        #imprime mensaje en consola
        print (f"{self._nombre} ha caminado {cant_pasos} pasos."+
            f"\nHa perdido {peso_perdido} grs. \nSu nuevo peso es de: {self._peso} kgs")

    def dormir(self, tiempo):
        """ Método: dormir del OBJ animal """
        print(f"{self._nombre} está cansado :( \nSe irá dormir.")
        print("Durmiendo ......")
        i = 0
        while i >= 0:
            if i < tiempo:
                i += 1
                print(f" {i} zzzZZzzz ")
            if i == tiempo:
                print(f"{self._nombre} ya está descansado :)")
                break
