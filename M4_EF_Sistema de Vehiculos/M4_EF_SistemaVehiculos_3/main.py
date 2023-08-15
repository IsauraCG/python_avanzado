""" Importaciones """
from modelo.automovil import Automovil
from modelo.particular import Particular
from modelo.carga import Carga
# from modelo.vehiculo import Vehiculo
from modelo.bicicleta import Bicicleta
from modelo.motocicleta import Motocicleta
from service.automovil_service import guardar , guardar_datos_csv, recuperar , imprimir_csv

# EJEMPLO
# automovil = Automovil("Ford", "Fiesta", "4", "180", "500")
# guardar("vehiculos.csv", automovil)
# automoviles = recuperar("vehiculos.csv")

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva",21,"Doble Viga","2T")

# print(particular)
# print(carga)
# print(bicicleta)
# print(motocicleta)

vehiculos = [particular,carga,bicicleta,motocicleta]
guardar_datos_csv(vehiculos,"vehiculos2.csv")

imprimir_csv("vehiculos2.csv")
