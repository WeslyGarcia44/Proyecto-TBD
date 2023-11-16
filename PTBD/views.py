

def home_view(request):
    # Asumiendo que tienes una plantilla 'home.html' en la carpeta de plantillas de tu aplicación o en la carpeta global de plantillas.
    return render(request, 'main/home.html')
from django.shortcuts import render

def login_view(request):
    return render(request, 'registration/login.html')
