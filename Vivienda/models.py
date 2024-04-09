from django.db import models

# Create your models here.

class Vivienda(models.Model):
    idVivienda = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=45)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.direccion 
    


class TipoVivienda(models.Model):
    idTipoVivienda = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    poblacion = models.IntegerField()

    def __str__(self):
        return self.direccion 