# Crear archivo y en caso de que existe lee la informacion
def crear_archivo():

    try:

        file = open('informacion.dat', 'x')  # crear el archivo y se apertura
        file.close()  # Cierra el archivo
    except FileExistsError:

        print('El archivo ya existe, ha sido creado previamente')

    except Exception as e:

        print(f'Error: {e}')

    if FileExistsError:

        try:

            with open('informacion.dat', 'r') as file:

                datos = file.readlines()

                for linea in datos:

                    print(linea)

        except Exception as e:

            print({e})


crear_archivo()
