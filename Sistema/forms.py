from django import forms
from .models import Cliente
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CrearCliente(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = [
            'rut',
            'nombre',
            'apellido',
            'telefono',
            'correo',
        ]
        labels = {
            'rut' : 'Rut',
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'telefono' : 'Celular',
            'correo' : 'Correo',
        }
        widgets = {
            'rut' : forms.TextInput(attrs={'class':'form'}),
            'nombre' : forms.TextInput(attrs={'class':'form'}),
            'apellido': forms.TextInput(attrs={'class':'form'}),
            'telefono' : forms.TextInput(attrs={'class':'form'}),
            'correo' : forms.TextInput(attrs={'class':'form'}),
        }