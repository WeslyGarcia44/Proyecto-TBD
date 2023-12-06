# tournaments/urls.py

from django.urls import path

from . import views
from .views import lista_torneos

urlpatterns = [
    path('', lista_torneos, name='lista-torneos'),
    path('tournaments/', views.tournaments_view, name='tournaments'),
    path('inscribir_torneo/<int:torneo_id>/', views.inscribir_torneo, name='inscribir_torneo'),
    path('inscribir_genesis_x/', views.inscribir_genesis_x, name='inscribir_genesis_x'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),

    # Agrega aquí más rutas según sea necesario
]
