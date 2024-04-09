from django.shortcuts import render, redirect
from .models import Barrio
from django.contrib import messages

# Create your views here.
def gestionBarrios(request):
    barrios = Barrio.objects.all()
    messages.success(request, '¡Viviendas listadas!')
    return render(request, 'gestionBarrios.html',{'barrios':barrios})

def registrarBarrio(request):
    direccion = request.POST['txtDireccion']
    capacidad = request.POST['txtCapacidad']
 #   persona = Persona.objects.create(
 #       direccion=direccion, capacidad=capacidad)
 #   messages.success(request, '¡Barrio registrado!')
    return redirect('/gestionBarrios')

def edicionBarrio(request, codigo):
 #   persona = Barrio.objects.get(codigo=codigo)
  #  return render(request, "edicionBarrio.html", {"persona": persona})
   pass

def editarBarrio(request):
    idBarrio = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
 #   persona = Barrio.objects.get(idBarrio=idBarrio)
 #   persona.nombre = nombre
 #   persona.creditos = creditos
 #   persona.save()
    messages.success(request, '¡Barrio actualizado!')
    return redirect('/')

def eliminarBarrio(request, idBarrio):
  #  persona = Barrio.objects.get(idBarrio=idBarrio)
  #  persona.delete()
    messages.success(request, '¡Barrio eliminado!')

    return redirect('/')
