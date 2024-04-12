from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Municipio
from django.contrib import messages
from Persona.models import Persona
from Departamento.models import Departamento

# Create your views here.
def gestionMunicipios(request):
    municipios = Municipio.objects.all()
    persona = Persona.objects.all()
    departamento = Departamento.objects.all()
    messages.success(request, '¡Viviendas listadas!')
    return render(request, 'gestionMunicipios.html',{'municipios':municipios,'persona':persona,'departamentos':departamento})

def registrarMunicipio(request):
    nombremunicipio = request.POST.get('txtNombreMunicipio')
    poblacion = request.POST.get('txtPoblacion')
    area = request.POST.get('txtArea')
    presupuesto = request.POST.get('txtPresupuesto')
    idPersona = request.POST.get('txtAlcalde')
    idDepartamento = request.POST.get('txtDepartamento')

    alcalde= None
    departamento = None

    try:
        alcalde = Persona.objects.get(idPersona=idPersona)
    except  ObjectDoesNotExist:
        pass

    try:
        departamento = Departamento.objects.get(idDepartamento=idDepartamento)
    except  ObjectDoesNotExist:
        pass

    municipio = Municipio.objects.create(
        nombreMunicipio=nombremunicipio,
        poblacion=poblacion,
        area=area,
        presupuesto=presupuesto,
        idAlcalde = alcalde,
        idDepartamento = departamento,
    )
    municipio.save()
    messages.success(request, '¡Municipio registrado!')
    return redirect('/gestionMunicipios')

def edicionMunicipio(request, idMunicipio):
    municipios = Municipio.objects.get(idMunicipio=idMunicipio)
    persona = Persona.objects.all()
    departamento = Departamento.objects.all()
    messages.success(request, '¡Viviendas listadas!')
    return render(request, 'edicionMunicipio.html',{'municipios':municipios,'persona':persona,'departamentos':departamento})





def editarMunicipio(request, idMunicipio):
    # Recuperar el municipio existente por su ID
    municipio = Municipio.objects.get(idMunicipio=idMunicipio)

    # Recuperar los datos del formulario
    nombre = request.POST.get('txtNombreMunicipio')
    poblacion = request.POST.get('txtPoblacion')
    area = request.POST.get('txtArea')
    presupuesto = request.POST.get('txtPresupuesto')
    idAlcalde = request.POST.get('txtAlcalde')
    idDepartamento = request.POST.get('txtDepartamento')


    municipio.nombreMunicipio = nombre
    municipio.poblacion = poblacion
    municipio.area = area
    municipio.presupuesto = presupuesto

    alcalde= None
    departamento = None

    try:
        alcalde = Persona.objects.get(idPersona=idAlcalde)
    except  ObjectDoesNotExist:
        pass

    try:
        departamento = Departamento.objects.get(idDepartamento=idDepartamento)
    except  ObjectDoesNotExist:
        pass

    municipio.idAlcalde = alcalde
    municipio.idDepartamento = departamento

    municipio.save()

    # Mostrar un mensaje de éxito y redirigir a la página de gestión de municipios
    messages.success(request, '¡Municipio actualizado!')
    return redirect('/gestionMunicipios')


def eliminarMunicipio(request, idMunicipio):
    municipio = Municipio.objects.get(idMunicipio=idMunicipio)
    if municipio.barrio_set.exists():
        municipio.barrio_set.update(idMunicipio=None)
    municipio.delete()
    messages.success(request, '¡Municipio eliminado!')

    return redirect('/gestionMunicipios')