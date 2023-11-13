
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class RangoUsuario(models.Model):
    nombre = models.CharField(max_length=255)
    nivel = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} (Nivel {self.nivel})"

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    correo_electronico = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    rango_usuario = models.ForeignKey(RangoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# Modelo para el perfil del usuario
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='user_avatars/', null=True, blank=True)
    # Otros campos adicionales que quieras incluir

    def __str__(self):
        return self.user.username

# Crear o actualizar el perfil del usuario automáticamente cada vez que se crea o actualiza un usuario.
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()


class Friendship(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friendships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friends', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Esto asegura que no podamos tener múltiples instancias de amistad con los mismos usuarios
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f"{self.from_user.username} es amigo de {self.to_user.username}"
