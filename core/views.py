from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def register_view(request):
    return render(request, 'register.html')

def proyecto_view(request):
    return render(request, 'proyecto.html')

def sensores_view(request):
    return render(request, 'sensores.html')

def appmovil_view(request):
    return render(request, 'appmovil.html')

def contacto_view(request):
    return render(request, 'contacto.html')




