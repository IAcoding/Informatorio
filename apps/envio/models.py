from django.db import models
from ..usuarios.models import Domicilio
from ..logistica.models import Carga, Transportista

#Ejemplo Vigente , Finalizado , etc
class Estado():
    nombre = models.CharField(unique=True, blank=False, max_length=20)

    def __str__(self):
        return self.nombre



#Ejemplo Urgente, entrega en 24hs, menor precio, Camion, etc.
class Etiqueta():
    nombre = models.CharField(unique=True, null=False, blank=False, max_length=20)

    def __str__(self):
        return self.nombre

#un envio tiene asignado un Transportista. que es el ganador y elegido de la subasta.
class Envio():
    origen = models.ForeignKey(Domicilio)
    destino = models.ForeignKey(Domicilio)
    tipo_carga = models.ForeignKey(Carga)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    subasta = models.BooleanField()
    etiquetas = models.ForeignKey(Etiqueta)
    observacion = models.TextField(null=True , max_length=500)
    trasnsportista = models.ForeignKey(Transportista, null=True)#queda en blanco de momento hasta que se termine la subasta

    def __str__(self):
        return self.origen + self.destino + self.estado + self.observacion



#una subasta se corresponde con un solo envio.
#una subasta tiene muchas ofertas
class Subasta():
    fecha_hora_inicio = models.DateTimeField()
    duracion = models.IntegerField()
    envio = models.OneToOneField(Envio, on_delete=models.CASCADE)


#una oferta de un transportista se corresponde con una sola subasta.
class Oferta():
    transportista = models.ForeignKey(Transportista)
    precio = models.FloatField(null=False)
    fecha_hora = models.DateTimeField(null=False)
    subasta = models.ForeignKey(Subasta)

    def __str__(self):
        return self.transportista + self.precio + self.fecha_hora
