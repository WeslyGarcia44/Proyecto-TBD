from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, nombre, correo_electronico, password=None):
        if not correo_electronico:
            raise ValueError('Los usuarios deben tener una dirección de correo electrónico')
        user = self.model(
            nombre=nombre,
            correo_electronico=self.normalize_email(correo_electronico),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, correo_electronico, password):
        user = self.create_user(
            nombre=nombre,
            correo_electronico=correo_electronico,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=255, unique=True)
    correo_electronico = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'nombre'
    REQUIRED_FIELDS = ['correo_electronico']

    def __str__(self):
        return self.nombre

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    def create_superuser(self, nombre, correo_electronico, password):
        user = self.create_user(
            nombre=nombre,
            correo_electronico=correo_electronico,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user







# Modelo para el perfil del usuario


# Crear o actualizar el perfil del usuario automáticamente cada vez que se crea o actualiza un usuario.



class Friendship(models.Model):
    from_user = models.ForeignKey(Usuario, related_name='friendships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(Usuario, related_name='friends', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f"{self.from_user.nombre} es amigo de {self.to_user.nombre}"


# Aquí puedes incluir otros modelos si los necesitas
