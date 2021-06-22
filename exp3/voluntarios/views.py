from django.shortcuts import redirect, render
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.   39:15

def index(request):

    return render(request, 'voluntarios/index.html')


def index3(request):
    
    usuarios = Usuario.objects.all()
    


    return render(request, 'voluntarios/index3.html', context = {'datos': usuarios})

def crearusuario(request):
    if request.method == 'POST':
        usuarioForm = UsuarioForm(request.POST)
        if usuarioForm.is_valid():
            usuarioForm.save()
            return redirect('crearusuario')
    else:
        usuarioForm=UsuarioForm()
    return render(request, 'voluntarios/crearusuario.html', {'usuario': usuarioForm})


def Ver(request):
    usuarios = Usuario.objects.all()
    return render(request, 'voluntarios/ver.html', context={'usuarios': usuarios})