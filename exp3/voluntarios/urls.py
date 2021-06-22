from django.urls import path
from .views import crearusuario, index, index3, Ver

urlpatterns = [
    path ('', index, name= "index"),
    path ('index3/', index3 , name="index3"),
    path('crearusuario/', crearusuario, name="crearusuario"),
    path('ver', Ver, name="ver"),
    
]

