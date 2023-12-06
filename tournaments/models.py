from django.db import models
from django.conf import settings
from users.models import Usuario

class Torneo(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    premio = models.TextField()

    def __str__(self):
        return self.nombre

class InscripcionTorneo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    torneo = models.ForeignKey('Torneo', on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} inscrito en {self.torneo.nombre}"
from django.shortcuts import render, get_object_or_404
from .models import InscripcionTorneo

def ver_inscripcion(request, inscripcion_id):
    # Obtiene una inscripción específica por su ID
    inscripcion = get_object_or_404(InscripcionTorneo, id=inscripcion_id)

    # Accede al nombre del torneo asociado a esa inscripción
    nombre_del_torneo = inscripcion.torneo.nombre

    # Pasa la inscripción y el nombre del torneo al contexto de la plantilla
    context = {
        'inscripcion': inscripcion,
        'nombre_del_torneo': nombre_del_torneo,
    }

    # Renderiza una plantilla, pasando el contexto
    return render(request, 'registration/perfil.html', context)
