from django.db import models
from Barrio.models import Barrio
# Create your models here.

class TipoVivienda(models.Model):
    idTipoVivienda = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45,null=True,blank=True)
    


class Vivienda(models.Model):
    idVivienda = models.AutoField(primary_key=True)
    #idPropietario = models.ForeignKey(Persona,null=True,blank=True)
    idBarrio = models.ForeignKey(Barrio,null=True,blank=True,on_delete=models.DO_NOTHING)
    idTipo_vivienda = models.ForeignKey(TipoVivienda,null=True,blank=True,on_delete=models.DO_NOTHING)
    direccion = models.CharField(max_length=45,null=True,blank=True)
    capacidad = models.IntegerField()



