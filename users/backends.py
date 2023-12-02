from django.contrib.auth.backends import BaseBackend
from .models import Usuario  # Asegúrate de importar tu modelo Usuario correctamente


class MyCustomBackend(BaseBackend):
    def authenticate(self, request, nombre=None, password=None):
        try:
            usuario = Usuario.objects.get(nombre=nombre)
            if usuario.contraseña == password:  # Verificación de contraseña
                return usuario
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
