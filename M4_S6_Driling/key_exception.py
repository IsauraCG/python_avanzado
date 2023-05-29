import pprint  # pprint da formato de impresión más legible al diccionario
# 1.-Se da el siguiente diccionario:
usuarios = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
# 2.-Intente imprimir el valor de la clave:
id_usuario = '004'
# 3.-En caso de KeyError, imprima en la consola el siguiente mensaje:
msg_error = "La clave '004' no está en el diccionario. Agregando clave..."
# 4.-Luego, agregue esta clave al diccionario con el valor “Ninguno”,
# e imprima el diccionario de usuarios en la consola.


# Se define método
def imprimir_usuario():
    """ Funcion imprimir usuario key '004' """
    # se establece estructura try - except
    try:
        # intente imprimir el key dado (inexistente)
        print(usuarios[id_usuario])
    except KeyError:            # "as e:" si queremos capturar el error en variable apra usarlo
        # se imprime el mensaje de error entregado
        print(f"{msg_error}")
        # se añade el elemento al diccionario
        usuarios.setdefault(id_usuario, None)
        # se imprime el nuevo diccionario con formato
        print("El diccionario queda: ")
        pprint.pprint(usuarios, indent=2, width=1)


imprimir_usuario()

# Métodos de formato para imprimir el diccionario

# 1 # PPRINT
# import pprint
#   pprint.pprint(usuarios)

# 2 # JSON.DUMPS
# print(json.dumps(usuarios, sort_keys=False, indent=4))

# 3 # PYYAML
# El nuevo parámetro default_flow_style, que determina si el estilo de salida del volcado
# debe ser inline o block.
# En este caso, la salida debe ser de estilo bloque ya que queremos que sea legible,
# así que establece este parámetro a False.

# pip3 install pyyaml
# import yaml
#   print(yaml.dump(usuarios, sort_keys=False, default_flow_style=False))
