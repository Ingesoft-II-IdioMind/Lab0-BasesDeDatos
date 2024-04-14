from Persona.models import Persona
from .models import PersonaVivienda,Vivienda


def setPropietario(idPersona,idVivienda):
    if idVivienda:
            try:
                idVivienda = int(idVivienda)
                vivienda = Vivienda.objects.get(idVivienda=idVivienda)
            except:
                vivienda = None
    if idPersona:
            try:
                idPersona = int(idPersona)
                persona = Persona.objects.get(idPersona=idPersona)
            except:
                persona = None        
    
    relacion = PersonaVivienda.objects.create(
         idVivienda=vivienda,
         idPersona=persona,
         residente = False,
         propietario=True,
         )
    relacion.save()
