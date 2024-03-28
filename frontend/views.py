from django.shortcuts import render, redirect
from .models import Barrio, Departamento, Municipio, Persona, Vivienda
from django.contrib import messages


# Create your views here.
def home(request):
    personas = Persona.objects.all()
    messages.success(request, '¡Personas listadas!')
    return render(request, 'gestionPersonas.html',{'personas':personas})

def registrarPersona(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    telefono = request.POST['txtTelefono']
    sexo = request.POST['txtSexo']
    edad = request.POST['txtEdad']

    persona = Persona.objects.create(
        nombre=nombre, apellido=apellido, telefono=telefono, sexo=sexo, edad=edad)
    messages.success(request, '¡Persona registrado!')
    return redirect('/')

def edicionPersona(request, codigo):
    persona = Persona.objects.get(codigo=codigo)
    return render(request, "edicionPersona.html", {"persona": persona})

def editarPersona(request):
    idPersona = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    persona = Persona.objects.get(idPersona=idPersona)
    persona.nombre = nombre
    persona.creditos = creditos
    persona.save()

    messages.success(request, '¡Persona actualizado!')

    return redirect('/')

def eliminarPersona(request, idPersona):
    persona = Persona.objects.get(idPersona=idPersona)
    persona.delete()
    messages.success(request, '¡Persona eliminado!')

    return redirect('/')

def gestionViviendas(request):
    viviendas = Vivienda.objects.all()
    messages.success(request, '¡Viviendas listadas!')
    return render(request, 'gestionViviendas.html',{'viviendas':viviendas})

def registrarVivienda(request):
    direccion = request.POST['txtDireccion']
    capacidad = request.POST['txtCapacidad']
    persona = Persona.objects.create(
        direccion=direccion, capacidad=capacidad)
    messages.success(request, '¡Vivienda registrado!')
    return redirect('/gestionViviendas')

def edicionVivienda(request, codigo):
    persona = Vivienda.objects.get(codigo=codigo)
    return render(request, "edicionVivienda.html", {"persona": persona})

def editarVivienda(request):
    idVivienda = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    persona = Vivienda.objects.get(idVivienda=idVivienda)
    persona.nombre = nombre
    persona.creditos = creditos
    persona.save()
    messages.success(request, '¡Vivienda actualizado!')
    return redirect('/')

def eliminarVivienda(request, idVivienda):
    persona = Vivienda.objects.get(idVivienda=idVivienda)
    persona.delete()
    messages.success(request, '¡Vivienda eliminado!')

    return redirect('/')

def gestionBarrios(request):
    barrios = Barrio.objects.all()
    messages.success(request, '¡Viviendas listadas!')
    return render(request, 'gestionBarrios.html',{'barrios':barrios})

def registrarBarrio(request):
    direccion = request.POST['txtDireccion']
    capacidad = request.POST['txtCapacidad']
    persona = Persona.objects.create(
        direccion=direccion, capacidad=capacidad)
    messages.success(request, '¡Barrio registrado!')
    return redirect('/gestionBarrios')

def edicionBarrio(request, codigo):
    persona = Barrio.objects.get(codigo=codigo)
    return render(request, "edicionBarrio.html", {"persona": persona})

def editarBarrio(request):
    idBarrio = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    persona = Barrio.objects.get(idBarrio=idBarrio)
    persona.nombre = nombre
    persona.creditos = creditos
    persona.save()
    messages.success(request, '¡Barrio actualizado!')
    return redirect('/')

def eliminarBarrio(request, idBarrio):
    persona = Barrio.objects.get(idBarrio=idBarrio)
    persona.delete()
    messages.success(request, '¡Barrio eliminado!')

    return redirect('/')

def gestionMunicipios(request):
    municipios = Municipio.objects.all()
    messages.success(request, '¡Viviendas listadas!')
    return render(request, 'gestionMunicipios.html',{'municipios':municipios, 'departamentos':Departamento.objects.all()})

def registrarMunicipio(request):
    direccion = request.POST['txtDireccion']
    capacidad = request.POST['txtCapacidad']
    persona = Persona.objects.create(
        direccion=direccion, capacidad=capacidad)
    messages.success(request, '¡Municipio registrado!')
    return redirect('/gestionMunicipios')

def edicionMunicipio(request, codigo):
    persona = Municipio.objects.get(codigo=codigo)
    return render(request, "edicionMunicipio.html", {"persona": persona})

def editarMunicipio(request):
    idMunicipio = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    persona = Municipio.objects.get(idMunicipio=idMunicipio)
    persona.nombre = nombre
    persona.creditos = creditos
    persona.save()
    messages.success(request, '¡Municipio actualizado!')
    return redirect('/')

def eliminarMunicipio(request, idMunicipio):
    persona = Municipio.objects.get(idMunicipio=idMunicipio)
    persona.delete()
    messages.success(request, '¡Municipio eliminado!')

    return redirect('/')

def gestionDepartamentos(request):
    departamentos = Departamento.objects.all()
    messages.success(request, '¡Viviendas listadas!')
    return render(request, 'gestionDepartamentos.html',{'departamentos':departamentos})

def registrarDepartamento(request):
    nombreDepartamento = request.POST['txtNombre']
    poblacion = request.POST['txtPoblacion']
    # idGobernador = request.POST['txtGobernador']
    idGobernador = Persona.objects.get(idPersona=request.POST['txtGobernador'])

    departamento = Departamento.objects.create(
        nombreDepartamento=nombreDepartamento, poblacion=poblacion, idGobernador=idGobernador)
    messages.success(request, '¡Departamento registrado!')
    return redirect('/gestionDepartamentos')

def edicionDepartamento(request, codigo):
    persona = Departamento.objects.get(codigo=codigo)
    return render(request, "edicionDepartamento.html", {"persona": persona})

def editarDepartamento(request):
    idDepartamento = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    persona = Departamento.objects.get(idDepartamento=idDepartamento)
    persona.nombre = nombre
    persona.creditos = creditos
    persona.save()
    messages.success(request, '¡Departamento actualizado!')
    return redirect('/')

def eliminarDepartamento(request, idDepartamento):
    departamento = Departamento.objects.get(idDepartamento=idDepartamento)
    departamento.delete()
    messages.success(request, '¡Departamento eliminado!')
    return redirect('/gestionDepartamentos')
