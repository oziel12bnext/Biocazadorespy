from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Usuario


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        username = request.POST.get("usuario")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        # Validación de contraseña
        if password != confirm:
            messages.error(request, "Las contraseñas no coinciden ❌")
            return redirect("register")

        # Validar usuario existente en Django Auth
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe ❌")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo ya está registrado ❌")
            return redirect("register")

        # Crear usuario en Django Auth (seguro)
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Guardar usuario en tu modelo personalizado
        Usuario.objects.create(
            nombre=nombre,
            correo=email,     # Asegúrate que tu modelo usa "correo"
            usuario=username
        )

        # Auto login
        login(request, user)

        messages.success(request, "Cuenta creada con éxito 🎉")
        return redirect("dashboard")

    return render(request, "register.html")



def dashboard(request):
    return render(request, "dashboard.html")


def sensores(request):
    return render(request, "sensores.html")


def contacto(request):
    return render(request, "contacto.html")


def proyecto(request):
    return render(request, "proyecto.html")
