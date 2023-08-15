"""
Rebound

Diseñe un programa en Python que cree un archivo si no se encuentra; en caso de existir el
archivo, debe reflejar un mensaje que especifica que ya se encuentra el archivo previamente
creado.
El archivo por crear debe llamarse 'informacion.dat' el cual contiene lo siguiente:
Datos de información en la línea 1
Datos de información en la línea 2
Datos de información en la línea 3
Datos de información en la línea 4
Datos de información en la línea 5
"""


def crear_archivo(lista):
    """ Crear archivo si no se encuentra """
    try:
        file = open('informacion.dat', 'x',
                    encoding='utf-8')  # crear el archivo
        with open('informacion.dat', 'w', encoding='utf-8') as file:
            for dato in lista:
                file.write(dato+"\n")
        file.close()  # cerrar el archivo
    except FileExistsError:
        print("El archivo 'informacion.dat' ya existe, ha sido creado previamente")


lista_datos = [
    'Datos de información en la línea 1',
    'Datos de información en la línea 2',
    'Datos de información en la línea 3',
    'Datos de información en la línea 4',
    'Datos de información en la línea 5'
]
crear_archivo(lista_datos)
