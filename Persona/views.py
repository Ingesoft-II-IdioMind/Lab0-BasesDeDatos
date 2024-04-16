from django.shortcuts import render, redirect
from .utils import setResidencia
from .models import Persona
from Vivienda.models import Vivienda,PersonaVivienda
from django.contrib import messages



def home(request):
    personas = Persona.objects.all()
    viviendas = Vivienda.objects.all()
    residentes = Persona.objects.filter(personavivienda__residente=True)
    contexto = {'personas': personas,'viviendas':viviendas,'residentes':residentes}
    return render(request, 'gestionPersonas.html', contexto)



def registrarPersona(request):
    if request.method == 'POST':
        idPersona = request.POST['txtNumeroIdentificacion']
        tipo_de_documento = request.POST['txtDocumento']
        nombre = request.POST['txtNombre']
        apellido = request.POST['txtApellido']
        telefono = request.POST['txtTelefono']
        sexo = request.POST.get('selectSexo')
        fecha_nacimiento = request.POST['fechaNacimiento']
        id_responsable = request.POST['txtCabezaIdentificacion']
        idVivienda = request.POST['txtRelacionvivienda']

        if Persona.objects.filter(idPersona=idPersona).exists():
            messages.error(request, 'El ID ya está en uso.')
            return redirect('/')
              
        # Crear la persona sin un responsable
        persona = Persona.objects.create(
            idPersona=idPersona,
            tipo_de_documento=tipo_de_documento,
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            sexo=sexo,
            fecha_nacimiento=fecha_nacimiento
        )
        setResidencia(idPersona,idVivienda)
        if id_responsable and id_responsable == idPersona:
            persona.idResponsable = persona
            persona.save()
        elif id_responsable:
            try:
                id_responsable_directo = int(id_responsable)
                responsable_directo = Persona.objects.get(pk=id_responsable_directo)
                persona.idResponsable = responsable_directo
                persona.save()
            except (ValueError, Persona.DoesNotExist):
                pass  
        messages.success(request, '¡Persona registrada!')
        return redirect('/')
    else:
        return render(request, 'gestionPersonas.html')



def edicionPersona(request,idPersona):
    persona = Persona.objects.get(idPersona=idPersona)
    viviendas = Vivienda.objects.all()
    
    return render(request, "edicionPersona.html", {"persona": persona,'viviendas':viviendas})

def editarPersona(request, idPersona):
    tipo_de_documento = request.POST['txtDocumento']
    nuevo_idPersona = request.POST['txtNumeroIdentificacion']
    nombre = request.POST['Nombre']
    apellido = request.POST['Apellido']
    telefono = request.POST['telefono']
    sexo = request.POST['sexo']
    fecha_nacimiento = request.POST['fechaNacimiento']
    id_responsable = request.POST.get('txtCabezaIdentificacion')
    idVivienda = request.POST.get('txtRelacionvivienda')

    responsable_directo = None
    if id_responsable:
        try:
            id_responsable_directo = int(id_responsable)
            responsable_directo = Persona.objects.get(pk=id_responsable_directo)
        except (ValueError, Persona.DoesNotExist):
            pass

    if Persona.objects.filter(idPersona=nuevo_idPersona).exclude(idPersona=idPersona).exists():
        messages.error(request, 'El nuevo ID ya está en uso.')
        return redirect(f'/edicionPersona/{idPersona}/')

    persona = Persona.objects.get(idPersona=idPersona)

    relacion = PersonaVivienda.objects.filter(idPersona=persona)
    if PersonaVivienda.objects.filter(idPersona=persona,residente = True ,propietario = True).exists():
       relacion=PersonaVivienda.objects.filter(idPersona=persona,residente = True ,propietario = True)
       relacion.residente = False
       relacion.idPersona = nuevo_idPersona
    elif PersonaVivienda.objects.filter(idPersona=persona,residente = True ,propietario = False).exists():
        ant=PersonaVivienda.objects.filter(idPersona=persona,residente = True ,propietario = False)
        ant.delete()
        setResidencia(nuevo_idPersona,idVivienda)

    persona.idPersona = nuevo_idPersona
    persona.tipo_de_documento = tipo_de_documento
    persona.nombre = nombre
    persona.apellido = apellido
    persona.telefono = telefono
    persona.sexo = sexo
    persona.fecha_nacimiento = fecha_nacimiento
    persona.idResponsable = responsable_directo

    persona.save()

    messages.success(request, '¡Persona actualizada!')
    return redirect('/')

def eliminarPersona(request, idPersona):
    persona = Persona.objects.get(idPersona=idPersona)
    if persona.departamento_set.exists():
        persona.departamento_set.update(idGobernador=None)
    if persona.municipio_set.exists():
        persona.municipio_set.update(idAlcalde=None)
    
    persona.delete()
    messages.success(request, '¡Persona eliminado!')

    return redirect('/')