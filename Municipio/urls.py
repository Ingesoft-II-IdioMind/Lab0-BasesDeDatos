from . import views
from django.urls import path 


urlpatterns = [
    path('gestionMunicipios/', views.gestionMunicipios),
    path('registrarMunicipio/', views.registrarMunicipio),
    path('edicionMunicipio/<int:idMunicipio>/', views.edicionMunicipio),
    path('editarMunicipio/<int:idMunicipio>/', views.editarMunicipio),
    path('eliminarMunicipio/<int:idMunicipio>/',views.eliminarMunicipio),
]