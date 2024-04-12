from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Barrio
from django.contrib import messages
from Municipio.models import Municipio

# Create your views here.
def gestionBarrios(request):
    barrios = Barrio.objects.all()
    municipios = Municipio.objects.all()
    messages.success(request, '¡Barrios listados!')
    return render(request, 'gestionBarrios.html', {'barrios': barrios, 'municipios': municipios})

def registrarBarrio(request):
    nombre_barrio = request.POST.get('txtNombreBarrio')
    poblacion = request.POST.get('txtPoblacion')
    id_municipio = request.POST.get('txtMunicipio')

    municipio = None

    try:
        municipio = Municipio.objects.get(idMunicipio=id_municipio)
    except ObjectDoesNotExist:
        pass

    barrio = Barrio.objects.create(
        nombreBarrio=nombre_barrio,
        poblacion=poblacion,
        idMunicipio=municipio,
    )
    barrio.save()
    messages.success(request, '¡Barrio registrado!')
    return redirect('/gestionBarrios')

def edicionBarrio(request, idBarrio):
    barrios = Barrio.objects.get(idBarrio=idBarrio)
    municipios = Municipio.objects.all()
    return render(request, "edicionBarrio.html", {"barrios":barrios,"municipios":municipios})


def editarBarrio(request,idBarrio):
    nombre_barrio = request.POST['txtNombreBarrio']
    poblacion = request.POST['txtPoblacion']
    id_municipio = request.POST.get('txtMunicipio')

    municipio = None

    try:
        municipio = Municipio.objects.get(idMunicipio=id_municipio)
    except ObjectDoesNotExist:
        pass

    barrio = Barrio.objects.get(idBarrio=idBarrio)
    barrio.nombreBarrio = nombre_barrio
    barrio.poblacion = poblacion
    barrio.idMunicipio = municipio
    barrio.save()


    messages.success(request, '¡Barrio actualizado!')
    return redirect('/gestionBarrios')

def eliminarBarrio(request, idBarrio):
    barrio = Barrio.objects.get(idBarrio=idBarrio)
  #  if barrio.vivienda_set.exists():
  #      barrio.vivienda_set.update(idBarrio=None)
    barrio.delete()
    messages.success(request, '¡Barrio eliminado!')

    return redirect('/gestionBarrios')
