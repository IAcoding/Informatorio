from django.db import models
from django.contrib.auth.models import User


class Localidad(models.Model):
    nombre = models.CharField(unique=True, blank=False, max_length=50)

    def __str__(self):
        return f"self.nombre"



class Provincia(models.Model):
    localidades = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    nombre = models.CharField(unique=True, blank=False, max_length=50)

    def __str__(self):
        return self.nombre



#los demas campos los hereda de abstract user ejemplo : nombre apellido etc.
class Transportista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cuit = models.CharField(unique=True, blank=False, max_length=11)
    fecha_nacimiento = models.DateField(blank=False)
    telefono = models.CharField(blank=False, max_length=15)

    def __str__(self):
        return self.cuit + self.username



#las empresas o particulares son las que hacen las ofertas de envios de productos.
class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cuit = models.CharField(unique=True, blank=False, max_length=11)
    telefono = models.CharField(blank=False, max_length=15)

    def __str__(self):
        return self.cuit + self.username



#observacion es un campo adicional para que la empresa coloque por ejemplo : sucursal Shopping center,
class Domicilio(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    calle = models.CharField(blank=False, max_length=30)
    altura = models.IntegerField()
    piso = models.IntegerField(blank=True)
    departamento = models.IntegerField(blank=True)
    observacion = models.CharField(blank=True, max_length=75)

    def __str__(self):
        return self.empresa + self.calle + self.altura + self.provincia + self.localidad

