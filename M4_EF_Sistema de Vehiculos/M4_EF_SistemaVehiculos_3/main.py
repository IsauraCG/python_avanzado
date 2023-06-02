""" Importaciones """
from modelo.automovil import Automovil
from modelo.particular import Particular
from modelo.carga import Carga
from modelo.vehiculo import Vehiculo
from modelo.bicicleta import Bicicleta
from modelo.motocicleta import Motocicleta


particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva",21,"Doble Viga","2T")

print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print(
    f"\nMotocicleta es instancia con relación a Vehículo: {isinstance(motocicleta,Vehiculo)}\n"+ 
    f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta,Automovil)}\n"+
    f"Motocicleta es instancia con relación a Vehículo Particular: {isinstance(motocicleta,Particular)}\n" + 
    f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta,Carga)}\n" + 
    f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta,Bicicleta)}\n" +
    f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta,Motocicleta)}\n"
)