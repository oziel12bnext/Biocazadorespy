from django.urls import path
from . import views
from .views import register_view


urlpatterns = [
      path('register/', register_view, name='register'),
    path('', views.home, name='home'),               # Página principal
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('proyecto/', views.proyecto, name='proyecto'),
    path('sensores/', views.sensores, name='sensores'),
    path('contacto/', views.contacto, name='contacto'),
]
