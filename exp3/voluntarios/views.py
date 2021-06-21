from django.shortcuts import render
from .models import Usuario

# Create your views here.   39:15

def index(request):

    return render(request, 'voluntarios/index.html')


def index3(request):
    
    usuarios = Usuario.objects.all()

    datos = {
        'usuarios' : usuarios
    }


    return render(request, 'voluntarios/index3.html', context = {'datos': usuarios})