# users/views.py

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# users/views.py

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Friendship
from django.shortcuts import render

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Asegúrate de que tienes una URL con nombre 'login'
    template_name = 'registration/signup.html'  # El template que crearemos a continuación


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Asegúrate de que 'login' es el nombre de la URL de tu vista de login
    template_name = 'registration/signup.html'
# users/views.py



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

def friend_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    friends = Friendship.objects.filter(from_user=user)  # O `to_user=user` dependiendo de cómo quieras definir "amigo"
    return render(request, 'users/friend_list.html', {'friends': friends})