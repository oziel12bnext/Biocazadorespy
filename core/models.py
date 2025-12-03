from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    usuario = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.usuario
