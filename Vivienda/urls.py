from . import views
from django.urls import path

urlpatterns = [
    path('gestionViviendas/', views.gestionViviendas),
    path('gestionViviendas/registrarVivienda/', views.registrarVivienda),
    path('gestionViviendas/edicionVivienda/<idVivienda>', views.edicionVivienda),
    path('gestionViviendas/editarVivienda/', views.editarVivienda),
    path('gestionViviendas/eliminarVivienda/<idVivienda>', views.eliminarVivienda),
]