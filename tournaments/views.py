from django.shortcuts import render
# tournaments/views.py

from django.shortcuts import render
from .models import Torneo

def lista_torneos(request):
    torneos = Torneo.objects.all().order_by('fecha_inicio')
    return render(request, 'tournaments/lista_torneos.html', {'torneos': torneos})

# Create your views here.
