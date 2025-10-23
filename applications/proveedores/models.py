from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.empresa})"
