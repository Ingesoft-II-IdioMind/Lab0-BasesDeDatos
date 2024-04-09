from django.db import models

# Create your models here.

class Persona(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('N','No especificado')
    ]

    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('N','No especificado')
        # Agrega más tipos de documentos según sea necesario
    ]

    idPersona = models.IntegerField(primary_key=True)
    idResponsable = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank = True, related_name='cabezaFamilia')
    nombre = models.CharField(max_length=50)
    tipo_de_documento = models.CharField(max_length=5,choices=TIPO_DOCUMENTO_CHOICES,default='N')
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10, default='Not specified')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES,default='N')
    edad = models.CharField(max_length=30, default='Not specified')

    def __str__(self):
        return self.nombre + ' ' + self.apellido
