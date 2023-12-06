from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Torneo, InscripcionTorneo
from django.contrib.auth.decorators import login_required

# tournaments/views.py

from django.shortcuts import render
from .models import Torneo


def lista_torneos(request):
    torneos = Torneo.objects.all().order_by('fecha_inicio')
    return render(request, 'tournaments/lista_torneos.html', {'torneos': torneos})


def tournaments_view(request):
    return render(request, 'Categories/Tournaments.html')


# Create your views here.
from .models import Torneo, InscripcionTorneo, Usuario  # Importa tu modelo Usuario si es necesario


def inscribir_torneo(request, torneo_id):
    if request.user.is_authenticated:
        torneo = Torneo.objects.get(id=torneo_id)
        InscripcionTorneo.objects.create(usuario=request.user, torneo=torneo)
        # Redirige a una página de confirmación o de vuelta al torneo
    else:
        return redirect('tournaments')




@login_required
def inscribir_genesis_x(request):
    torneo = get_object_or_404(Torneo, id=1)  # ID del torneo Genesis X
    InscripcionTorneo.objects.create(usuario=request.user, torneo=torneo)
    # Redirige a una página de confirmación o de vuelta al torneo
    return redirect('tournaments')


from django.shortcuts import render
from .models import InscripcionTorneo


from django.shortcuts import render
from .models import InscripcionTorneo
@login_required
def perfil_usuario(request):
    inscripciones_usuario = InscripcionTorneo.objects.filter(usuario=request.user).select_related('torneo')
    # Otros contextos pueden ser agregados aquí también
    return render(request, 'registration/perfil.html', {'inscripciones_usuario': inscripciones_usuario})

def tu_vista(request):
    inscripciones_usuario = InscripcionTorneo.objects.filter(usuario=request.user).select_related('torneo')
    context = {
        'inscripciones_usuario': inscripciones_usuario,
    }
    return render(request, 'registration/perfil.html', context)
@login_required
def vista_torneos(request):
    inscripciones_usuario = InscripcionTorneo.objects.filter(usuario=request.user).select_related('torneo')
    return render(request, 'registration/perfil.html', {'inscripciones_usuario': inscripciones_usuario})
def ver_inscripcion(request, inscripcion_id):
    # Obtiene una inscripción específica por su ID
    inscripcion = get_object_or_404(InscripcionTorneo, id=1)
    # Accede al nombre del torneo asociado a esa inscripción
    nombre_del_torneo = inscripcion.torneo.nombre

    # Pasa la inscripción y el nombre del torneo al contexto de la plantilla
    context = {
        'inscripcion': inscripcion,
        'nombre_del_torneo': nombre_del_torneo,
    }

    # Renderiza una plantilla, pasando el contexto
    return render(request, 'registration/perfil.html', context)




from django.contrib.auth.decorators import login_required
from .models import InscripcionTorneo, Torneo

@login_required
def perfil_usuario(request):
    # Obtén todas las inscripciones del usuario actual
    inscripciones_usuario = InscripcionTorneo.objects.filter(usuario=request.user).select_related('torneo')

    # Crear una lista de nombres de torneos en los que está inscrito el usuario
    nombres_torneos = [inscripcion.torneo.nombre for inscripcion in inscripciones_usuario]

    context = {
        'nombres_torneos': nombres_torneos,
    }

    return render(request, 'registration/perfil.html', context)
