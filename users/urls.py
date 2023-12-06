from django.urls import path

from . import views
from .views import (
    login_view,
    send_friend_request,
    accept_friend_request,
    friend_list,
    signup_view,
    home_view
)

urlpatterns = [
    path('send-friend-request/<int:user_id>/', send_friend_request, name='send-friend-request'),
    path('accept-friend-request/<int:friendship_id>/', accept_friend_request, name='accept-friend-request'),
    path('friends/<int:user_id>/', friend_list, name='friend-list'),
    path('signup/', signup_view, name='signup'),
    path('home/', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('users/', views.user_list_view, name='list_friends'),
    path('add-friend/<int:user_id>/', views.add_friend, name='add-friend'),
    path('friends/', views.friends_list_view, name='friends-list'),
    path('perfil/', views.friends_list_view, name='perfil'),
    path('logout/', views.custom_logout, name='logout'),

    # ... otras URLs de la aplicación 'users' si las hay ...
]
