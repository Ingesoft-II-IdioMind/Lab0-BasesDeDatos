from . import views
from django.urls import path

urlpatterns = [
    path('gestionBarrios/', views.gestionBarrios),
    path('registrarBarrio/', views.registrarBarrio),
    path('edicionBarrio/<int:idBarrio>', views.edicionBarrio),
    path('editarBarrio/<int:idBarrio>', views.editarBarrio),
    path('eliminarBarrio/<int:idBarrio>', views.eliminarBarrio),
]