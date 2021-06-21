# Generated by Django 3.1.6 on 2021-06-21 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rutUsuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut de usuario')),
                ('nombreUsuario', models.CharField(max_length=50, verbose_name='Nombre de usuario')),
                ('fechaNac', models.DateField(verbose_name='Fecha de nacimiento')),
                ('region', models.CharField(max_length=20, verbose_name='Región')),
                ('comuna', models.CharField(max_length=20, verbose_name='Comuna')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('email2', models.EmailField(max_length=254, verbose_name='Reingrese su Email')),
                ('password', models.CharField(max_length=12, verbose_name='Password')),
                ('password2', models.CharField(max_length=12, verbose_name='Reingrese su Password')),
                ('fono', models.CharField(max_length=12, verbose_name='Número de teléfono')),
                ('vol_ayuda', models.CharField(choices=[('VO', 'Quiero ser voluntario'), ('AY', 'Necesito ayuda')], default='VO', max_length=2)),
            ],
        ),
    ]
