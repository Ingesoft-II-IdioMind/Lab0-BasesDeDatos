from . import views
from django.urls import path

urlpatterns = [
    path('gestionBarrios/', views.gestionBarrios),
    path('gestionBarrios/registrarBarrio/', views.registrarBarrio),
    path('gestionBarrios/edicionBarrio/<idBarrio>', views.edicionBarrio),
    path('gestionBarrios/editarBarrio/', views.editarBarrio),
    path('gestionBarrios/eliminarBarrio/<idBarrio>', views.eliminarBarrio),
]