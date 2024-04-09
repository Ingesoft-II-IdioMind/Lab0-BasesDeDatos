from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('registrarPersona/', views.registrarPersona),
    path('edicionPersona/<int:idPersona>/', views.edicionPersona),
    path('editarPersona/<int:idPersona>/', views.editarPersona),
    path('eliminarPersona/<int:idPersona>', views.eliminarPersona),
]