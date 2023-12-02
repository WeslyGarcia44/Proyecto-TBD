from django.shortcuts import render

def c_view(request):
    # Aquí puedes añadir cualquier lógica que necesites
    return render(request, 'Community/c.html')
