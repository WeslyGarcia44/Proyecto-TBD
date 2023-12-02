from django.urls import path
from . import views

urlpatterns = [
    path('c/', views.c_view, name='c'),
]
