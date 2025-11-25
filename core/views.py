from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect



def register_view(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        usuario = request.POST.get("usuario")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect("register")

        # Puedes agregar más validaciones aquí

        # Crear usuario
        try:
            User.objects.create_user(username=usuario, email=email, password=password, first_name=nombre)
            messages.success(request, "Cuenta creada correctamente.")
            return redirect("home")  # O a donde quieras
        except Exception as e:
            messages.error(request, "Error al crear usuario: " + str(e))
            return redirect("register")

    return render(request, "register.html")

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
