from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('proyecto/', views.proyecto_view, name='proyecto'), 
    path('sensores/', views.sensores_view, name='sensores'),
    path('appmovil/', views.appmovil_view, name='appmovil'), 
    path('contacto/', views.contacto_view, name='contacto'), 
    
    ]
