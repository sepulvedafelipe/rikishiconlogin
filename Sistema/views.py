from django.shortcuts import render,redirect
from .models import Cliente
from .forms import CrearCliente
"""from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm"""
from django.db.models import DEFERRED
from django.core import serializers
import json
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout

# Create your views here.
def inicio(request):
    return render (request,"inicio.html")

    
def base_layout(request):
    return render(request,"maqueta.html")



def registroCliente(request):
    form=CrearCliente(request.POST or None)
    if form.is_valid():
        datos=form.cleaned_data
        regDb=Cliente(rut=datos.get("rut"),nombre=datos.get("nombre"),apellido=datos.get("apellido"),
        telefono=datos.get("telefono"),correo=datos.get("correo"))
        regDb.save()
    cliente=Cliente.objects.all()
    contexto={
        'cliente':cliente,
        'form':form,
    }
    return render (request,"registroCliente.html",contexto)

def loginCliente(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request,'loginCliente.html', {'form':form})


def logoutCliente(request):
    if request.method == 'POST':
        logout(request)
        return redirect('inicio')