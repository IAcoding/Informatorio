from django.db import models
from ..usuarios.models import Transportista

# Create your models here.

class Modelo(models.Model):
    nombre = models.CharField(unique=True, blank=False , max_length=50)

    def __str__(self):
        return self.nombre



class Marca(models.Model):
    nombre = models.CharField(unique=True, blank=False, max_length=25)
    modelos = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre



#Cargas son los tipos de cargas que existen Ej: Carga Pesada , inflamable, carga peligrosa, fragil.
class Carga(models.Model):
    nombre = models.CharField(unique=True, blank=False, max_length=50)

    def __str__(self):
        return self.nombre



class Vehiculo(models.Model):
    patente = models.CharField(unique=True, blank=False, max_length=7)
    acoplado = models.BooleanField()
    capacidad_max = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Transportista, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente + self.capacidad_max + self.cargas_aceptadas + self.propietario


