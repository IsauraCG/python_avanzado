""" Automovil Service """
from parte_1.modelo.automovil import Automovil


class AutomovilService:
    """ Clase Automovil Service """

    def solicitar_cantidad(self) -> int:
        """ Función que pide una cantidad de vehículos a crear y retorna esa cantidad """
        # Solicitud de la cantidad de vehículos a ingresar
        cantidad = int(input("¿Cuántos vehículos desea insertar? : "))
        # print(cantidad)
        return cantidad

    def solicitar_datos(self) -> Automovil:
        """ Función que pide los datos al usuario"""
        marca_solicitada = input("\tIngrese la marca: ")
        modelo_solicitado = input("\tIngrese el modelo: ")
        ruedas_solicitadas = input("\tIngrese la cantidad de ruedas: ")
        velocidad_solicitada = input("\tIngrese velocidad max. en km/hr: ")
        cilindrada_solicitada = input("\tIngrese cilindrada en cc: ")
        automovil = Automovil(marca=marca_solicitada,
                              modelo=modelo_solicitado,
                              numero_ruedas=ruedas_solicitadas,
                              velocidad=velocidad_solicitada,
                              cilindrada=cilindrada_solicitada)
        # print(automovil)
        return automovil

    def crear_automoviles(self, lista_autos) -> list:
        """ Función que crea determinada cantidad de automoviles"""
        # Listado de vehículos
        dict_auto = {}
        lista_autos = []
        # declaración de variable de control 'cantidad'
        contador = 0
        # declaración de variable que contendrá
        # el valor retornado por la función 'solicitar_cantidad'
        cantidad_a_ingresar = AutomovilService.solicitar_cantidad(self)
        # ciclo que condiciona su ejecución según qué valor contenga 'cantidad'
        # se ejecuta mientras 'cantidad' sea menor que 'cantidad_a_ingresar'
        while contador < cantidad_a_ingresar:
            # iteración del valor en 'cantidad'
            contador += 1
            # impresión de mensaje por consola
            print(f"\nDatos del automóvil {contador}")
            # se solicitan los datos para crear un nuevo automovil
            automovil_creado = AutomovilService.solicitar_datos(self)
            # añade el nuevo automovil (formado desde 'solicitar_datos'),
            # a la lista 'listado_autos'
            dict_auto[contador] = {
                "Marca": automovil_creado.marca,
                "Modelo": automovil_creado.modelo,
                "N° de Ruedas": automovil_creado.numero_ruedas,
                "Velocidad": automovil_creado.velocidad,
                "Cilindrada": automovil_creado.cilindrada}
            lista_autos.append(dict_auto[contador])
            # impresion del nuevo automovil creado
            # print(str(f"\t{automovil_creado}"))
            print(" -- Automovil Creado Exitosamente -- ")
        # para un impresión ordenada y con formato de la lista con cada nuevo automovil:
        # import pprint
        # pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
        # pp.pprint(lista_autos)
        # # pp.pprint(dict_auto)
        return lista_autos

    def imprimir_automoviles_dict(self, lista_autos):
        """ Función que recibe una lista e imprime los vehículos en ella """
        i = 0
        print("\nImprimiendo por pantalla los Vehículos: ")
        for auto in lista_autos:
            i += 1
            print(f"Datos del automóvil {i} : " +
                  f"Marca {auto.get('Marca')}, " +
                  f"Modelo {auto.get('Modelo')}, " +
                  f"{auto.get('N° de Ruedas')} ruedas, " +
                  f"Velocidad {auto.get('Velocidad')} Km/h, " +
                  f"Cilindrada {auto.get('Cilindrada')} cc."
                  )
        print("\n")

    def imprimir_lista_automoviles(self):
        """ Función que recibe una lista e imprime los vehículos en ella """
        # Se genera lista para ejecutar función con los datos del ejercicio
        lista_autos = [
            # Instancias de obj Automovil
            Automovil("Toyota", "Yaris", 4, 120, 800),
            Automovil("Fiat", "Palio", 4, 95, 1200),
            Automovil("Ford", "Fiesta", 4, 125, 1500),
        ]
        # variable de iteración
        i = 0
        # Mensaje de inicio
        print("\nImprimiendo por pantalla los Vehículos: ")
        # Ciclo que imprime cada elemento en la lista
        for auto in lista_autos:
            i += 1
            print(f"Datos del automóvil {i} : " +
                  f"Marca {auto.marca}, " +
                  f"Modelo {auto.modelo}, " +
                  f"{auto.numero_ruedas} ruedas, " +
                  f"Velocidad {auto.velocidad} Km/h, " +
                  f"Cilindrada {auto.cilindrada} cc."
                  )
        print("\n")
