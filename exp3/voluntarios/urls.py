from django.urls import path
from .views import crearusuario, form_del_usuario, index, index3, Ver,form_mod_usuario

urlpatterns = [
    path ('', index, name= "index"),
    path ('index3/', index3 , name="index3"),
    path('crearusuario/', crearusuario, name="crearusuario"),
    path('ver', Ver, name="ver"),
    path('form_del_usuario/<id>', form_del_usuario, name="form_del_usuario"),
    path('form_mod_usuario/<id>',form_mod_usuario, name="form_mod_usuario")
    
]

