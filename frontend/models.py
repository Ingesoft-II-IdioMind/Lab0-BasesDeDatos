from django.db import models

class Persona(models.Model):
    idPersona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10, default='Not specified')
    sexo = models.CharField(max_length=30, default='Not specified')
    edad = models.CharField(max_length=30, default='Not specified')

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Vivienda(models.Model):
    idVivienda = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=45)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.direccion 
    
class Barrio(models.Model):
    idBarrio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    poblacion = models.IntegerField()

    def __str__(self):
        return self.direccion 

class Municipio(models.Model):
    idMunicipio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    poblacion = models.IntegerField()

    def __str__(self):
        return self.direccion 
    
class Departamento(models.Model):
    idDepartamento = models.AutoField(primary_key=True)
    nombreDepartamento = models.CharField(max_length=45)
    poblacion = models.IntegerField(default=0)
    #idGobernador = models.ForeignKey(Persona, default=0, on_delete=models.DO_NOTHING)
    #genenera conflictos mirar como arreglar
    def __str__(self):
        return self.nombreDepartamento
    
class TipoVivienda(models.Model):
    idTipoVivienda = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    poblacion = models.IntegerField()

    def __str__(self):
        return self.direccion 