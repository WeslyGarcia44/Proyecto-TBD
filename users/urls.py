# users/urls.py

from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LoginView
from .views import edit_user_profile
from . import views

urlpatterns = [

    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('edit_profile/', edit_user_profile, name='edit-profile'),
    path('send-friend-request/<int:user_id>/', views.send_friend_request, name='send-friend-request'),
    path('accept-friend-request/<int:friendship_id>/', views.accept_friend_request, name='accept-friend-request'),
    path('friends/<int:user_id>/', views.friend_list, name='friend-list'),
    # ... otras URLs de la aplicación 'users' ...
]
