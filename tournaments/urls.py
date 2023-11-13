# tournaments/urls.py

from django.urls import path
from .views import lista_torneos

urlpatterns = [
    path('', lista_torneos, name='lista-torneos'),
    # Agrega aquí más rutas según sea necesario
]
