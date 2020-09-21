from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Localidad():
    nombre = models.TextField(unique=True, blank=False)


class Provincia():
    nombre = models.TextField(unique=True, blank=False)
    localidades = models.ForeignKey(Localidad, on_delete=models.CASCADE)



#los demas campos los hereda de abstract user ejemplo : nombre apellido etc.
class Transportista(AbstractUser):
    cuit = models.TextField(unique=True, blank=False, max_length=11)
    fecha_nacimiento = models.DateField(blank=False)
    telefono = models.TextField(blank=False, max_length=15)


#las empresas o particulares son las que hacen las ofertas de envios de productos.
class Empresa(AbstractUser):
    cuit = models.TextField(unique=True, blank=False, max_length=11)
    telefono = models.TextField(blank=False, max_length=15)



#observacion es un campo adicional para que la empresa coloque por ejemplo : sucursal Shopping center,
class Domicilio():
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    calle = models.TextField(blank=False, max_length=30)
    altura = models.IntegerField()
    piso = models.IntegerField(blank=True)
    departamento = models.IntegerField(blank=True)
    observacion = models.TextField(blank=True, max_length=75)
