from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect


def home(request):
    return render(request, "home.html")

def register(request):
    return render(request, "register.html")

def dashboard(request):
    return render(request, "dashboard.html")

def sensores(request):
    return render(request, "sensores.html")

def contacto(request):
    return render(request, "contacto.html")

def proyecto(request):
    return render(request, "proyecto.html")
