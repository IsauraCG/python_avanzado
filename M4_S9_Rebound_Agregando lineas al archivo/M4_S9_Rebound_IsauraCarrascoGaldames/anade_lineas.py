""" Diseñe un programa en Python que agregue el siguiente contenido al archivo:
informacion.dat.

Hola Mundo 
Esta es una nueva línea en el archivo
Agregando la segunda línea del archivo
Finalizando la línea agregada 
"""


def agregar_info_linea(texto):
    """  Agrega solo una linea """
    try:
        with open("informacion.dat", "a", encoding="utf8") as file:
            file.write(f"{texto}\n")
    except FileNotFoundError:
        print("Error: Archivo no encontrado")


agregar_info_linea("Hola Mundo")
agregar_info_linea("Esta es una nueva línea en el archivo")
agregar_info_linea("Agregando la segunda línea del archivo")
agregar_info_linea("Finalizando la línea agregada")
