from django import forms
from django.forms import ModelForm, widgets
from .models import Usuario


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['rutUsuario', 'nombreUsuario',
                  'fechaNac', 'region', 'comuna',
                  'email', 'email2', 'password',
                  'password2', 'fono']

        labels = {
            'rutUsuario': 'RUT',
            'nombreUsuario': 'Nombre de usuario', 
            'fechaNac': 'Fecha de nacimiento',
            'region': 'Región', 
            'comuna': 'Comuna',
            'email': 'Email',
            'email2': 'Reingrese su email',
            'password': 'Contraseña',
            'password2': 'Reingrese su contraseña',
            'fono': 'Número de teléfono'
        }

        widgets = {
            'rutUsuario': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su rut con guión y sin puntos',
                    'id': 'rutUsuario'

                }
            ),
            'nombreUsuario': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'id': 'nombreUsuario'
                }
            ),
            'fechaNac': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'Ingrese su fecha de nacimiento',
                    'id': 'fechaNac'
                }
            ),
            'region': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su región',
                    'id': 'region'
                }
            ),
            'comuna': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su comuna',
                    'id': 'comuna'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo electrónico',
                    'id': 'email',
                    'type': 'email'
                }
            ),
            'email2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Vuelva a ingresar su correo electrónico',
                    'id': 'region'
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su contraseña',
                    'id': 'password',
                    'type': 'password'
                }
            ),
            'password2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Vuelva a ingresar su contraseña',
                    'id': 'password2',
                    'type': 'password'
                }
            ),
            'fono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de teléfono',
                    'id': 'fono'
                }
            ),

        }
