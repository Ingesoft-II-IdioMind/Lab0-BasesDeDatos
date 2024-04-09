from django.db import models

# Create your models here.
class Municipio(models.Model):
    idMunicipio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    poblacion = models.IntegerField()

    def __str__(self):
        return self.direccion 
    
