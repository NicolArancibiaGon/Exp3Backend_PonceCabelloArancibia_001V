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


def form_del_usuario(request,id):
    usuario = Usuario.objects.get(rutUsuario=id)
    usuario.delete()
    return redirect('ver')

def form_mod_usuario(request,id):
    usuario = Usuario.objects.get(rutUsuario=id)

    datos={
        'form': UsuarioForm(instance=usuario)
    
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance = usuario)
        if formulario.is_valid:
            formulario.save()
            return redirect('ver')
    return render(request, 'voluntarios/form_mod_usuario.html', datos)