from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .models import Usuario, Friendship
from django.contrib.auth import logout


def signup_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo_electronico = request.POST.get('correo_electronico')
        contraseña = request.POST.get('contraseña')

        usuario = Usuario(nombre=nombre, correo_electronico=correo_electronico)
        usuario.set_password(contraseña)
        usuario.save()

        return redirect('home')

    return render(request, 'registration/signup.html')


# El resto de tus vistas aquí, con los cambios recomendados


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
            print("Inicio de sesión exitoso para:", nombre)  # Mensaje de éxito
            return redirect('perfil')
        else:
            print("Inicio de sesión fallido para:", nombre)  # Mensaje de fallo
            messages.error(request, 'Nombre o contraseña incorrectos.')

    return render(request, 'registration/login.html')


def perfil_view(request):
    return render(request, 'registration/perfil.html')


from users.models import Usuario


def user_list_view(request):
    users = Usuario.objects.all()  # Obtiene todos los usuarios
    return render(request, 'registration/library/friends.html', {'users': users})


from django.shortcuts import get_object_or_404, redirect
from .models import Usuario, Friendship


def add_friend(request, user_id):
    to_user = get_object_or_404(Usuario, id=user_id)
    from_user = request.user  # Usuario actualmente logueado
    # Verifica que no exista ya una amistad y que no seas tú mismo
    if from_user != to_user and not Friendship.objects.filter(from_user=from_user, to_user=to_user).exists():
        Friendship.objects.create(from_user=from_user, to_user=to_user)
    return redirect('list_friends')  # Redirige a alguna vista, por ejemplo, la lista de usuarios


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Friendship

User = get_user_model()


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Friendship, Usuario
@login_required
def friends_list_view(request):
    # Obtener las amistades donde el usuario actual es el 'from_user'
    friendships = Friendship.objects.filter(from_user=request.user)

    # Ahora, vamos a obtener los amigos (usuarios 'to_user') de esas instancias de Friendship
    friends = [friendship.to_user for friendship in friendships]

    context = {
        'friends': friends,
    }

    return render(request, 'registration/perfil.html', context)

def custom_logout(request):
    logout(request)
    return redirect('home')