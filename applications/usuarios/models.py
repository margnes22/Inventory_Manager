from django.db import models

# Create your models here.

class Usuario(models.Model):

    ROLES = [
        ('1', 'Vendedor'),
        ('2', 'Administrador'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    rol = models.CharField(max_length=50, choices=ROLES, default='vendedor')

    def __str__(self):
        return self.nombre
