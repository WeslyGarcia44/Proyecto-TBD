# PTBD/urls.py
from django.urls import include, path
from django.contrib import admin
from django.urls import path, include
from . import views  # Importa la vista desde el mismo nivel del proyecto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Incluye las URLs de la aplicación 'users'
    path('', views.home_view, name='home'),
    path('tournaments/', include('tournaments.urls')),
    # ... otras rutas de inclusión para tus aplicaciones ...
]