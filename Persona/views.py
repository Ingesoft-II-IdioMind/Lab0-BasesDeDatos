from django.shortcuts import render, redirect
from .models import Persona
from django.contrib import messages



def home(request):
    personas = Persona.objects.all()
    messages.success(request, '¡Personas listadas!')
    return render(request, 'gestionPersonas.html',{'personas':personas})

def registrarPersona(request):
    idPersona = request.POST['txtNumeroIdentificacion']
    tipo_de_documento = request.POST['txtDocumento']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    telefono = request.POST['txtTelefono']
    sexo = request.POST.get('selectSexo')
    edad = request.POST['txtEdad']

    Persona.objects.create(
        idPersona=idPersona, tipo_de_documento=tipo_de_documento,  nombre=nombre, apellido=apellido, telefono=telefono, sexo=sexo, edad=edad)
    messages.success(request, '¡Persona registrado!')
    return redirect('/')

def edicionPersona(request,idPersona):
    persona = Persona.objects.get(idPersona=idPersona)
    return render(request, "edicionPersona.html", {"persona": persona})

def editarPersona(request, idPersona):
    nombre = request.POST['Nombre']#dentro de las comillas debe ir el name no el id
    apellido = request.POST['Apellido']
    telefono = request.POST['telefono']
    sexo = request.POST['sexo']
    edad = request.POST['edad']
    persona = Persona.objects.get(idPersona=idPersona)
    persona.nombre = nombre
    persona.apellido = apellido
    persona.telefono = telefono
    persona.sexo = sexo
    persona.edad = edad
    persona.save()
    messages.success(request, '¡Persona actualizado!')
    return redirect('/')

def eliminarPersona(request, idPersona):
    persona = Persona.objects.get(idPersona=idPersona)
    persona.delete()
    messages.success(request, '¡Persona eliminado!')

    return redirect('/')