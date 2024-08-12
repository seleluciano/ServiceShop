from django.shortcuts import render
from appserviceshop.models import *
#from django.contrib.auth import authenticate, login
#from django.contrib.auth.forms import AuthenticationForm
#from .forms import UserRegisterForm
#from django.contrib.auth.decorators import login_required
#from django.views.generic import ListView
#from django.views.generic.edit import UpdateView, DeleteView,CreateView
#from django.views.generic.detail import DetailView
#from django.contrib.auth.mixins import LoginRequiredMixin


def Inicio(request):
    return render(request, "index.html")
