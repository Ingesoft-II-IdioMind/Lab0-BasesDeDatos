from django.shortcuts import render, redirect
from .models import Departamento
from django.contrib import messages

# Create your views here.
def gestionDepartamentos(request):
    departamentos = Departamento.objects.all()
  #  persona = Persona.objects.all()
    messages.success(request, '¡Viviendas listadas!')
    return render(request, 'gestionDepartamentos.html',{'departamentos':departamentos})

def registrarDepartamento(request):
    nombreDepartamento = request.POST['txtNombre']
    poblacion = request.POST['txtPoblacion']
 #   idGobernador = Persona.objects.get(idPersona=request.POST['txtGobernador'])

    departamento = Departamento.objects.create(
        nombreDepartamento=nombreDepartamento, poblacion=poblacion)
    messages.success(request, '¡Departamento registrado!')
    return redirect('/gestionDepartamentos')

def edicionDepartamento(request, idDepartamento):
    departamento = Departamento.objects.get(idDepartamento = idDepartamento)
  #  persona = Persona.objects.all()
    return render(request,"edicionDepartamento.html",{"Departamento":departamento})

def editarDepartamento(request,idDepartamento):
    nombre = request.POST['txtNombre']
    poblacion = request.POST['numPoblacion']
   # idGobernador = Persona.objects.get(idPersona=request.POST['txtGobernador'])
    departamento = Departamento.objects.get(idDepartamento=idDepartamento)
    departamento.nombreDepartamento = nombre
    departamento.poblacion = poblacion
 #   departamento.idGobernador = idGobernador
    departamento.save()
    messages.success(request, '¡Departamento actualizado!')
    return redirect('/gestionDepartamentos')

def eliminarDepartamento(request, idDepartamento):
    departamento = Departamento.objects.get(idDepartamento=idDepartamento)
    departamento.delete()
    messages.success(request, '¡Departamento eliminado!')
    return redirect('/gestionDepartamentos')
