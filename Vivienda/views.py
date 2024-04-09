from django.shortcuts import render, redirect
from .models import Vivienda
from django.contrib import messages
# Create your views here.
def gestionViviendas(request):
    viviendas = Vivienda.objects.all()
    messages.success(request, '¡Viviendas listadas!')
    return render(request, 'gestionViviendas.html',{'viviendas':viviendas})

def registrarVivienda(request):
    direccion = request.POST['txtDireccion']
 #   capacidad = request.POST['txtCapacidad']
 #   persona = Persona.objects.create(
 #       direccion=direccion, capacidad=capacidad)
 #   messages.success(request, '¡Vivienda registrado!')
 #   return redirect('/gestionViviendas')

def edicionVivienda(request, codigo):
 #   persona = Vivienda.objects.get(codigo=codigo)
 #   return render(request, "edicionVivienda.html", {"persona": persona})
    pass

def editarVivienda(request):
    idVivienda = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
  #  persona = Vivienda.objects.get(idVivienda=idVivienda)
  #  persona.nombre = nombre
  #  persona.creditos = creditos
  #  persona.save()
    messages.success(request, '¡Vivienda actualizado!')
    return redirect('/')

def eliminarVivienda(request, idVivienda):
   # persona = Vivienda.objects.get(idVivienda=idVivienda)
   # persona.delete()
    messages.success(request, '¡Vivienda eliminado!')

    return redirect('/')