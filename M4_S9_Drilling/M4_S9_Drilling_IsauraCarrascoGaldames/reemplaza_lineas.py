def reemplazar_datos(texto1, texto2):
    """ Función  que  reemplaza  el contenido de un archivo.
        texto1 se reemplaza por texto2
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


reemplazar_datos("información", "procesamiento")
