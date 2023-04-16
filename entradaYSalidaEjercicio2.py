#importamos pickle
import pickle
# Creamos la clase vehiculo


class vehiculo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}, precio: {self.precio}"
# Instanciamos un objeto de la clase
vehiculo1 = vehiculo("porche", 80000)

# Serializamos el objeto
with open("vehiculos.pickle","wb") as vehiculosGuardados:
    pickle.dump(vehiculo1, vehiculosGuardados)
