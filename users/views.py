# users/views.py

from .forms import UserProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Friendship
from django.contrib.auth.models import User
from .models import Usuario
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def signup_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo_electronico = request.POST.get('correo_electronico')
        contraseña = request.POST.get('contraseña')

        # Aquí puedes añadir validaciones adicionales si es necesario

        # Crear un nuevo usuario en tu modelo personalizado
        usuario = Usuario(nombre=nombre, correo_electronico=correo_electronico, contraseña=contraseña)
        usuario.save()

        # Redireccionar después del registro exitoso
        return redirect('home')

    return render(request, 'registration/signup.html')


def home_view(request):
    return render(request, 'main/home.html')


def edit_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('alguna_vista_post_edicion')
    else:
        form = UserProfileForm(instance=request.user.profile)

    return render(request, 'users/edit_profile.html', {'form': form})


# Vista para enviar una solicitud de amistad
def send_friend_request(request, user_id):
    from_user = request.user
    to_user = get_object_or_404(User, id=user_id)
    friendship, created = Friendship.objects.get_or_create(from_user=from_user, to_user=to_user)
    return redirect('alguna_vista')  # Redirige a la página deseada


# Vista para aceptar una solicitud de amistad (podría requerir lógica adicional)
def accept_friend_request(request, friendship_id):
    friendship = get_object_or_404(Friendship, id=friendship_id, to_user=request.user)
    friendship.save()  # Aquí podrías cambiar el estado de la solicitud, si tienes tal campo
    return redirect('alguna_vista')


# Vista para ver la lista de amigos
def friend_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    friends = user.friends.all()  # Basado en la relación inversa definida en el modelo Friendship
    return render(request, 'users/friend_list.html', {'friends': friends})


def login_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        password = request.POST.get('password')
        user = authenticate(request, nombre=nombre, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nombre o contraseña incorrectos.')

    return render(request, 'registration/login.html')
