from django.shortcuts import render, redirect
from .models import Municipio
from django.contrib import messages

# Create your views here.
def gestionMunicipios(request):
    municipios = Municipio.objects.all()
    messages.success(request, '¡Viviendas listadas!')
    return render(request, 'gestionMunicipios.html',{'municipios':municipios})

def registrarMunicipio(request):
    direccion = request.POST['txtDireccion']
    capacidad = request.POST['txtCapacidad']
  #  persona = Persona.objects.create(
  #      direccion=direccion, capacidad=capacidad)
    messages.success(request, '¡Municipio registrado!')
    return redirect('/gestionMunicipios')

def edicionMunicipio(request, codigo):
#    persona = Municipio.objects.get(codigo=codigo)
#    return render(request, "edicionMunicipio.html", {"persona": persona})
    pass

def editarMunicipio(request):
    idMunicipio = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
#    persona = Municipio.objects.get(idMunicipio=idMunicipio)
#    persona.nombre = nombre
#    persona.creditos = creditos
#    persona.save()
    messages.success(request, '¡Municipio actualizado!')
    return redirect('/')

def eliminarMunicipio(request, idMunicipio):
  #  persona = Municipio.objects.get(idMunicipio=idMunicipio)
  #  persona.delete()
    messages.success(request, '¡Municipio eliminado!')

    return redirect('/')