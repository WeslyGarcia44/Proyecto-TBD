# games/urls.py

from django.urls import path
from . import views
from django.urls import path
from .views import view_user_game_list
from .views import Games_

# "app_name = 'games'
urlpatterns = [
    path('add-game/<int:game_id>/', views.add_game_to_user_list, name='add-game-to-list'),
    # ... otras URLs para la aplicación de juegos ...
    path('my-games/', view_user_game_list, name='view-user-game-list'),
    path('games/', views.Games_, name='Games_'),

]
