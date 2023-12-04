from django.contrib.auth.backends import BaseBackend
from .models import Usuario

class MyCustomBackend(BaseBackend):
    def authenticate(self, request, nombre=None, password=None):
        try:
            usuario = Usuario.objects.get(nombre=nombre)
            if usuario.check_password(password):  # Verificación segura de contraseña
                return usuario
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
