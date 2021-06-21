from django.db import models

# Create your models here.

class Usuario(models.Model):
    rutUsuario = models.IntegerField(primary_key=True, verbose_name='Rut de usuario')
    nombreUsuario = models.CharField(max_length=50, verbose_name='Nombre de usuario')
    fechaNac = models.DateField()
    region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    email = models.EmailField()
    email2 = models.EmailField()
    password = models.CharField(max_length=12)
    password2 = models.CharField(max_length=12)
    fono = models.CharField(max_length=12)
    VOLUNTARIO = 'VO'
    AYUDA = 'AY'
    vol_ayuda_choices = [
        (VOLUNTARIO, 'Quiero ser voluntario'),
        (AYUDA, 'Necesito ayuda')
    ]
    vol_ayuda = models.CharField(
        max_length=2,
        choices= vol_ayuda_choices,
        default=VOLUNTARIO,
    )

    def str(self):
        return self.rutUsuario