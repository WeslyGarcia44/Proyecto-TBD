# games/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game, UserGameList
from django.shortcuts import render
from .models import UserGameList

@login_required
def add_game_to_user_list(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    user_game_list, created = UserGameList.objects.get_or_create(user=request.user, game=game)
    if created:

        pass
    return redirect('alguna_vista_para_ver_la_lista')  # Redirige a la vista donde el usuario puede ver su lista de juegos

def view_user_game_list(request):
    game_list = UserGameList.objects.filter(user=request.user)
    return render(request, 'games/user_game_list.html', {'game_list': game_list})
