from django.shortcuts import render, redirect
from .models import Departamento
from django.contrib import messages
from Persona.models import Persona

# Create your views here.
def gestionDepartamentos(request):
    departamentos = Departamento.objects.all()
    persona = Persona.objects.all()
    messages.success(request, '¡Viviendas listadas!')
    return render(request, 'gestionDepartamentos.html',{'departamentos':departamentos,'persona':persona})

from django.core.exceptions import ObjectDoesNotExist



def registrarDepartamento(request):
    nombreDepartamento = request.POST.get('txtNombre')
    poblacion = request.POST.get('txtPoblacion')
    idPersona = request.POST.get('txtGobernador')

    gobernador = None
    try:
        gobernador = Persona.objects.get(idPersona=idPersona)
    except ObjectDoesNotExist:
        # Log the error or handle it as needed
        pass

    departamento = Departamento.objects.create(
        nombreDepartamento=nombreDepartamento,
        poblacion=poblacion,
        idGobernador=gobernador
    )

    messages.success(request, '¡Departamento registrado!')
    return redirect('/gestionDepartamentos')




def edicionDepartamento(request, idDepartamento):
    departamento = Departamento.objects.get(idDepartamento = idDepartamento)
  #  persona = Persona.objects.all()
    return render(request,"edicionDepartamento.html",{"Departamento":departamento})

def editarDepartamento(request, idDepartamento):
    nombre = request.POST.get('txtNombre')
    poblacion = request.POST.get('numPoblacion')
    idPersona = request.POST.get('txtGobernador')

    gobernador = None
    try:
        gobernador = Persona.objects.get(idPersona=idPersona)
    except ObjectDoesNotExist:
        # Log the error or handle it as needed
        pass

    departamento = Departamento.objects.get(idDepartamento=idDepartamento)
    departamento.nombreDepartamento = nombre
    departamento.poblacion = poblacion
    departamento.idGobernador = gobernador
    departamento.save()

    messages.success(request, '¡Departamento actualizado!')
    return redirect('/gestionDepartamentos')

def eliminarDepartamento(request, idDepartamento):
    departamento = Departamento.objects.get(idDepartamento=idDepartamento)
    departamento.delete()
    messages.success(request, '¡Departamento eliminado!')
    return redirect('/gestionDepartamentos')
