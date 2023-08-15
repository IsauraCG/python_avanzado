def reemplazar_datos(texto1, texto2):
    """ Función  que  reemplaza  el contenido de un archivo.
        texto1 se reemplaza por texto2,
        sin alterar contenido del archivo.
    """
    contador = 0
    try:
        archivo = open("informacion.dat", "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()
        texto_reemplazado = ""
        for linea in lineas:
            if texto1 in linea:
                linea = linea.replace(texto1, texto2)
                texto_reemplazado += linea
                cantidad_de_lineas_final += 1
                contador += 1
            if contador > 0:
                archivo_modificado = open(
                    "informacion.dat", "w", encoding="utf-8")
                archivo_modificado.write(texto_reemplazado)
                archivo_modificado.close()
    except FileNotFoundError:
        print('No se encuentra el archivo datos.cvs')
    # except Exception as error:
    #     print('Se ha generado un error no previsto', type(error).__name__)
    finally:
        print("Se realizaron", contador, "reemplazos")


def contador_de_lineas():
    """ Función que captura, imprime y retorna la cantidad de lineas de contenido 
    en el archivo orginal 
    retorna : lineas"""
    contador = 0
    try:
        archivo = open("informacion.dat", "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()
        contador = len(lineas)
        print(f"El archivo original tiene {contador} lineas de contenido.")
        for linea in lineas:
            if "\n" in linea:
                linea = linea.replace("\n", " ")
            print(f"\t{linea}")
            lineas.append(linea)

        print(lineas)
    except Exception:
        print("Error")

    return lineas


def reemplaza_texto_en_linea(texto1, texto2):
    """ Función que reemplaza el texto1 en una línea, 
    por texto2 """
    lineas = contador_de_lineas
    for linea in lineas:
        if texto1 in linea:
            linea = linea.replace(texto1, texto2)


contador_de_lineas()
