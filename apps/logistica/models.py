from django.db import models
from ..usuarios.models import Transportista

# Create your models here.

class Modelo():
    nombre = models.TextField(unique=True, blank=False)


class Marca():
    nombre = models.TextField(unique=True, blank=False, max_length=15)
    modelos = models.ForeignKey(Modelo, on_delete=models.CASCADE)


#Cargas son los tipos de cargas que existen Ej: Carga Pesada , inflamable, carga peligrosa, fragil.
class Carga():
    nombre = models.TextField(unique=True, blank=False)



class Vehiculo():
    patente = models.TextField(unique=True, blank=False, max_length=7)
    acoplado = models.BooleanField()
    capacidad_max = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cargas_aceptadas = models.ForeignKey(Carga, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Transportista, on_delete=models.CASCADE)

