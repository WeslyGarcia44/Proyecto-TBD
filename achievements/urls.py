# achievements/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Aquí incluirías tus patrones de URL para la aplicación 'achievements'
    path('test/', views.test_view, name='test'),  # Asegúrate de tener una vista test_view en views.py
]
