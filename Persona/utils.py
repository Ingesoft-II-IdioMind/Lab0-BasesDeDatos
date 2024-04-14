from .models import Persona
from Vivienda.models import PersonaVivienda,Vivienda


def setResidencia(idPersona,idVivienda):
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
                idPersona = None        
    
    relacion = PersonaVivienda.objects.create(
         idVivienda=vivienda,
         idPersona=persona,
         residente = True,
         propietario=False,
         )
    relacion.save()
