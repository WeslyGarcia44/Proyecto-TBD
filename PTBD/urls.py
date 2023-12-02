# PTBD/urls.py
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Incluye las URLs de la aplicación 'users'
    path('', views.home_view, name='home'),
    path('tournaments/', include('tournaments.urls')),
    path('', include('achievements.urls')),
    path('login/', views.login_view, name='login'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tournaments/', views.tournaments_view, name='tournaments'),
    path('communities/', include('Communities.urls')),


    # ... otras rutas de inclusión para tus aplicaciones ...
]