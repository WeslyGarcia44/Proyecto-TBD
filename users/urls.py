from django.urls import path
from .views import (
    login_view,
    edit_user_profile,
    send_friend_request,
    accept_friend_request,
    friend_list,
    signup_view,
    home_view
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('edit_profile/', edit_user_profile, name='edit-profile'),
    path('send-friend-request/<int:user_id>/', send_friend_request, name='send-friend-request'),
    path('accept-friend-request/<int:friendship_id>/', accept_friend_request, name='accept-friend-request'),
    path('friends/<int:user_id>/', friend_list, name='friend-list'),
    path('signup/', signup_view, name='signup'),
    path('home/', home_view, name='home'),
    # ... otras URLs de la aplicación 'users' si las hay ...
]
