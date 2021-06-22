from django.db import models

# Create your models here.

class Usuario(models.Model):
    rutUsuario = models.CharField(primary_key=True, max_length=10,  verbose_name='Rut de usuario')
    nombreUsuario = models.CharField(max_length=50, verbose_name='Nombre de usuario')
    fechaNac = models.DateField(verbose_name='Fecha de nacimiento')
    region = models.CharField(max_length=20, verbose_name='Región')
    comuna = models.CharField(max_length=20, verbose_name='Comuna')
    email = models.EmailField(verbose_name='Email')
    email2 = models.EmailField(verbose_name='Reingrese su Email')
    password = models.CharField(max_length=12, verbose_name='Password')
    password2 = models.CharField(max_length=12, verbose_name='Reingrese su Password')
    fono = models.CharField(max_length=12, verbose_name='Número de teléfono')
   

    def __str__(self):
        return self.rutUsuario
