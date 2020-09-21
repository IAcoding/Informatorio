from django.db import models
from ..usuarios.models import Domicilio
from ..logistica.models import Carga, Transportista


class Estado():
    nombre = models.TextField(unique=True, blank=False, max_length=20)


class Envio():
    origen = models.ForeignKey(Domicilio)
    destino = models.ForeignKey(Domicilio)
    tipo_carga = models.ForeignKey(Carga)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    subasta = models.BooleanField()


class Oferta:
    transportista = models.ForeignKey(Transportista)
    precio = models.FloatField(null=False)
    fecha_hora = models.DateTimeField(null=False)

#FALTA HACER LA SUBASTA , QUE TIENE QUE ESTAR CONDICIONADO POR EL ENVIO, ES DECIR
#SI LA EMPRESA DESEA SUBASTAR EL ENVIO O BUSCAR EN LA LISTA DE TRANSPORTISTAS Y ELEGIR ALGUNO.