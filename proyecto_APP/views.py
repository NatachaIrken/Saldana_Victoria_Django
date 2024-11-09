from django.shortcuts import redirect, render
from proyecto_APP.models import Persona
from proyecto_APP.forms import FormPersona

def index(request):
    return render(request, 'index.html')

def listaPersona(request):
    persona = Persona.objects.all()
    data = {'perso': persona}
    return render(request, 'ListarPersonas.html', data) 

def agregarPersona(request):
    if request.method == 'POST':
        formP = FormPersona(request.POST)
        if formP.is_valid():
            formP.save()
            return redirect('listar_personas')  
    else:
        formP = FormPersona() 
    return render(request, 'agregarPersonas.html', {'formP': formP})



def eliminarPersona(request, id):
    try:
        persona = Persona.objects.get(id=id)
    except Persona.DoesNotExist:
        return redirect('listar_personas')  

    if request.method == 'POST':
        persona.delete()
        return redirect('listar_personas')  

    return render(request, 'eliminarPersonas.html', {'persona': persona}) 

def actualizarPersona(request, id):
    try:
        persona = Persona.objects.get(id=id)
    except Persona.DoesNotExist:
        return redirect('listar_personas') 

    if request.method == 'POST':
        form = FormPersona(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('listar_personas')
    else:
        form = FormPersona(instance=persona)

    return render(request, 'actualizarPersonas.html', {'form': form, 'persona': persona})
