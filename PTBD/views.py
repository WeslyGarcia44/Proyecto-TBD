from django.contrib.auth.models import User
from django.shortcuts import render

from games.models import Game


def home_view(request):
    # Asumiendo que tienes una plantilla 'home.html' en la carpeta de plantillas de tu aplicación o en la carpeta global de plantillas.
    return render(request, 'main/home.html')


def login_view(request):
    return render(request, 'registration/login.html')


def tournaments_view(request):
    return render(request, 'Categories/Tournaments.html')


from django.shortcuts import render


def signup_view(request):
    # Tu lógica para manejar el registro
    return render(request, 'registration/signup.html')


def Games_(request):
    games = Game.objects.all()
    return render(request, 'registration/library/games.html')


def user_list_view(request):
    users = User.objects.all()  # Obtiene todos los usuarios
    return render(request, 'registration/library/friends.html', {'users': users})
