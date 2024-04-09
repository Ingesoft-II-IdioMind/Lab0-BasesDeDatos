from django.db import models

# Create your models here.
class Departamento(models.Model):
    idDepartamento = models.AutoField(primary_key=True)
    nombreDepartamento = models.CharField(max_length=45)
    poblacion = models.IntegerField(default=0)
   # idGobernador = models.ForeignKey(Persona,null=True,blank = True, on_delete=models.DO_NOTHING)
    #genenera conflictos mirar como arreglar
    def __str__(self):
        return self.nombreDepartamento