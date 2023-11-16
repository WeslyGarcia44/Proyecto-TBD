# achievements/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Icluir patrones de URL para la aplicación 'achievements'
    path('test/', views.test_view, name='test'),
]
