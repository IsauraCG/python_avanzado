from modelo.cliente import Cliente


class ClienteService:

    # carga de archivo, lectura y creacion si el archivo no existe
    def load_clientes(self):
        try:
            with open('clientes.txt', 'r') as file:
                # apertura y cierra el archivo, se puede establecer el tipo de apertura
                file.readlines()
                # retorna una lista de tipo str
        except FileNotFoundError:
            print("Error loading (cargando) cliente")
