# Generated by Django 3.2.3 on 2021-06-21 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voluntarios', '0003_auto_20210621_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='voluntario_o_solicita',
        ),
    ]
