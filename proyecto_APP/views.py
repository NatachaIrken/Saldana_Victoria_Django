from django.shortcuts import redirect, render
from proyecto_APP.models import Persona

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listaPersona(request):
    persona = Persona.objects.all()
    data = {'perso': persona}
    return render(request, 'ListarPersonas.html', data)