from . import views
from django.urls import path

urlpatterns = [
    path('gestionDepartamentos/', views.gestionDepartamentos),
    path('registrarDepartamento/', views.registrarDepartamento),
    path('edicionDepartamento/<int:idDepartamento>/', views.edicionDepartamento),
    path('editarDepartamento/<int:idDepartamento>/', views.editarDepartamento),
    path('eliminarDepartamento/<int:idDepartamento>', views.eliminarDepartamento),
]
