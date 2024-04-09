from . import views
from django.urls import path 


urlpatterns = [
    path('gestionMunicipios/', views.gestionMunicipios),
    path('gestionMunicipios/registrarMunicipio/', views.registrarMunicipio),
    path('gestionMunicipios/edicionMunicipio/<idMunicipio>', views.edicionMunicipio),
    path('gestionMunicipios/editarMunicipio/', views.editarMunicipio),
    path('gestionMunicipios/eliminarMunicipio/<idMunicipio>', views.eliminarMunicipio),
]