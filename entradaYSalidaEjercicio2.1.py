#importamos pickle
import pickle


# Creamos la clase vehiculo
class vehiculo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}, precio: {self.precio}"
    
#Deserializamos el objeto vehiculo1
with open("vehiculos.pickle", "rb") as vehiculosGuardados:
    datos_guardados = pickle.load(vehiculosGuardados)
print(datos_guardados)
