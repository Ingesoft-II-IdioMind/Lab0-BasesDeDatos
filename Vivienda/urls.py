from . import views
from django.urls import path

urlpatterns = [
    path('gestionViviendas/', views.gestionViviendas),
    path('registrarVivienda/', views.registrarVivienda),
    path('edicionVivienda/<int:idVivienda>/', views.edicionVivienda),
    path('editarVivienda/<int:idVivienda>/', views.editarVivienda),
    path('eliminarVivienda/<int:idVivienda>/', views.eliminarVivienda),
]