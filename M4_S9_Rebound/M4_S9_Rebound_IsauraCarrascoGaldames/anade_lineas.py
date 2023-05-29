""" Diseñe un programa en Python que agregue el siguiente contenido al archivo:
informacion.dat.

Hola Mundo 
Esta es una nueva línea en el archivo
Agregando la segunda línea del archivo
Finalizando la línea agregada 
"""


def agregar_info_line(texto):
    """  Agrega solo una linea """
    try:
        with open("informacion.dat", "a", encoding="utf8") as file:
            file.write(texto+"\n")
    except FileNotFoundError:
        print("EROR FILE NOT FOUND")


agregar_info_line("Hola Mundo")
agregar_info_line("Esta es una nueva línea en el archivo")
agregar_info_line("Agregando la segunda línea del archivo")
agregar_info_line("Finalizando la línea agregada")
