from django.shortcuts import render,redirect
from .models import Perfil
from .forms import SignUpForm
"""from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm"""
from django.db.models import DEFERRED
from django.core import serializers
import json
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def inicio(request):
    return render (request,"inicio.html")

    
def base_layout(request):
    return render(request,"maqueta.html")

'''class registroCliente(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('inicio')
'''

def registroCliente(request):
    form=SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
    user=User.objects.all()
    contexto={
        'user':User,
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