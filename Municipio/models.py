from django.db import models
from Persona.models import Persona
from Departamento.models import Departamento

# Create your models here.
class Municipio(models.Model):
    idMunicipio = models.AutoField(primary_key=True)
    idAlcalde = models.ForeignKey(Persona,null=True,blank = True, on_delete=models.DO_NOTHING)
    idDepartamento = models.ForeignKey(Departamento,null=True, blank=True, on_delete=models.DO_NOTHING)
    area = models.FloatField(null=True, blank=True)
    presupuesto = models.FloatField(null=True, blank=True)
    nombreMunicipio = models.CharField(max_length=45,null=True, blank=True)
    poblacion = models.IntegerField(null=True, blank=True)

    
    