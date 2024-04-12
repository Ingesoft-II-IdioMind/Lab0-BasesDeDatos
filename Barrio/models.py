from django.db import models
from Municipio.models import Municipio

# Create your models here.
class Barrio(models.Model):
    idBarrio = models.AutoField(primary_key=True)
    idMunicipio = models.ForeignKey(Municipio,null=True, blank=True, on_delete=models.DO_NOTHING)
    nombreBarrio = models.CharField(max_length=45,null=True, blank=True)
    poblacion = models.IntegerField(null=True, blank=True)