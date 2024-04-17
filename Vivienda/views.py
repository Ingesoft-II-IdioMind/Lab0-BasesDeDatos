from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from Persona.models import Persona
from .models import Vivienda,TipoVivienda,PersonaVivienda
from .utils import setPropietario
from Barrio.models import Barrio
from django.contrib import messages
# Create your views here.
def gestionViviendas(request):
    viviendas = Vivienda.objects.all()
    persona = Persona.objects.all()
    barrios = Barrio.objects.all()
    propietarios = Persona.objects.filter(personavivienda__propietario=True)
    tipoviviendas = TipoVivienda.objects.all() 
    # messages.success(request, '¡Viviendas listadas!')
    return render(request, 'gestionViviendas.html',{'viviendas':viviendas,'barrios':barrios,'tipoviviendas':tipoviviendas,'personas':persona,'propietarios':propietarios})

def registrarVivienda(request):
    idBarrio = request.POST.get('txtidBarrio')
    idtipovivienda = request.POST.get('txtidTipovivienda')
    idPropietario = request.POST.get('txtPropietario')
    direccion = request.POST.get('txtDireccion')
    capacidad = request.POST.get('txtCapacidad')

    tipovivienda = None
    barrio = None

    try:
        tipovivienda = TipoVivienda.objects.get(idTipoVivienda=idtipovivienda)
    except  ObjectDoesNotExist:
        pass
    try:
        barrio = Barrio.objects.get(idBarrio=idBarrio)
    except  ObjectDoesNotExist:
        pass

    vivienda = Vivienda.objects.create(
        idBarrio=barrio,
        idTipo_vivienda=tipovivienda,
        direccion=direccion,
        capacidad=capacidad,
    )

    setPropietario(idPropietario,vivienda.idVivienda)
    vivienda.save()

    messages.success(request, '¡Vivienda registrada!')
    return redirect('/gestionViviendas')
 

def edicionVivienda(request, idVivienda):
    viviendas = Vivienda.objects.get(idVivienda=idVivienda)
    barrios = Barrio.objects.all()
    tipoviviendas = TipoVivienda.objects.all()
    # messages.success(request, '¡Viviendas listadas!')
    return render(request, 'edicionVivienda.html',{'viviendas':viviendas,'barrios':barrios,'tipoviviendas':tipoviviendas})


def editarVivienda(request,idVivienda):
    idBarrio = request.POST.get('txtidBarrio')
    idtipovivienda = request.POST.get('txtidTipovivienda')
    idPropietario = request.POST.get('txtPropietario')
    direccion = request.POST.get('txtDireccion')
    capacidad = request.POST.get('txtCapacidad')

    tipovivienda = None
    barrio = None

    try:
        tipovivienda = TipoVivienda.objects.get(idTipoVivienda=idtipovivienda)
    except  ObjectDoesNotExist:
        pass
    try:
        barrio = Barrio.objects.get(idBarrio=idBarrio)
    except  ObjectDoesNotExist:
        pass


    vivienda = Vivienda.objects.get(idVivienda=idVivienda)

    if PersonaVivienda.objects.filter(idVivienda=vivienda,residente = True ,propietario = True).exists():
       relacion=PersonaVivienda.objects.filter(idVivienda=vivienda,residente = True ,propietario = True)
       relacion.propietario = False
       relacion.idPersona = idPropietario
    elif PersonaVivienda.objects.filter(idVivienda=vivienda,residente = False ,propietario = True).exists():
        ant=PersonaVivienda.objects.filter(idVivienda=vivienda,residente = False ,propietario = True)
        ant.delete()
        setPropietario(idPropietario,idVivienda)

    vivienda.idBarrio = barrio
    vivienda.idTipo_vivienda = tipovivienda
    vivienda.direccion = direccion
    vivienda.capacidad = capacidad
    vivienda.save()
    messages.success(request, '¡Vivienda actualizado!')
    return redirect('/gestionViviendas')

def eliminarVivienda(request, idVivienda):
    vivienda = Vivienda.objects.get(idVivienda=idVivienda)
    vivienda.delete()
    messages.success(request, '¡Vivienda eliminado!')

    return redirect('/gestionViviendas')
