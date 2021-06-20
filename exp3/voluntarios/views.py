from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'voluntarios/index.html')

def index3(request):
    return render(request, 'voluntarios/index3.html')