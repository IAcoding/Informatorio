from django.db import models
from ..usuarios.models import Domicilio
from ..logistica.models import Carga, Transportista

#Ejemplo Vigente , Finalizado , etc
class Estado(models.Model):
    nombre = models.CharField(unique=True, blank=False, max_length=20)

    def __str__(self):
        return self.nombre



#Ejemplo Urgente, entrega en 24hs, menor precio, Camion, etc.
class Etiqueta(models.Model):
    nombre = models.CharField(unique=True, null=False, blank=False, max_length=20)

    def __str__(self):
        return self.nombre

#un envio tiene asignado un Transportista. que es el ganador y elegido de la subasta.
class Envio(models.Model):
    origen = models.ForeignKey(Domicilio, on_delete=models.CASCADE, related_name='origen_set')
    destino = models.ForeignKey(Domicilio, on_delete=models.CASCADE, related_name='destino_set')
    tipo_carga = models.ForeignKey(Carga, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    etiquetas = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
    observacion = models.TextField(null=True , max_length=500)
    trasnsportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)#queda en blanco de momento hasta que se termine la subasta

    def __str__(self):
        return self.origen + self.destino + self.estado + self.observacion



#una subasta se corresponde con un solo envio.
#una subasta tiene muchas ofertas
class Subasta(models.Model):
    fecha_hora_inicio = models.DateTimeField()
    duracion = models.IntegerField()
    envio = models.OneToOneField(Envio, on_delete=models.CASCADE)


#una oferta de un transportista se corresponde con una sola subasta.
class Oferta(models.Model):
    transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)
    precio = models.FloatField(null=False)
    fecha_hora = models.DateTimeField(null=False)
    subasta = models.ForeignKey(Subasta, on_delete=models.CASCADE)

    def __str__(self):
        return self.transportista + self.precio + self.fecha_hora
