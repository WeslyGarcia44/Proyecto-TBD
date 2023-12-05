
from django.conf import settings
from django.db import models
from tenants.models import Tenant

class GeneroVideojuego(models.Model):
   # tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=255, primary_key=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Videojuego(models.Model):
    #tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True)
    # Añadido para multi-tenancy
    titulo = models.CharField(max_length=255)
    fecha_lanzamiento = models.DateField()
    descripcion = models.TextField()
    genero_videojuego = models.ForeignKey(GeneroVideojuego, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

class Game(models.Model):
    #tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True)
    # Añadido para multi-tenancy
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    # Puedes agregar más campos según sea necesario

    def __str__(self):
        return self.title

class UserGameList(models.Model):
    #tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True)
    # Añadido para multi-tenancy
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True) #

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"
