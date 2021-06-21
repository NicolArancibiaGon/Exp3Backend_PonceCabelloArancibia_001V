# Generated by Django 3.2.4 on 2021-06-21 01:49

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
                ('fechaNac', models.DateField()),
                ('region', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
                ('password2', models.CharField(max_length=12)),
                ('fono', models.CharField(max_length=12)),
                ('vol_ayuda', models.CharField(choices=[('VO', 'Quiero ser voluntario'), ('AY', 'Necesito ayuda')], default='VO', max_length=2)),
            ],
        ),
    ]