from django.db import models
from django.conf import settings
from django.utils import timezone
from applications.productos.models import Producto  # asegúrate de tener esta app

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='ventas')
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fecha_venta = models.DateTimeField(default=timezone.now)
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.producto.nombre} ({self.cantidad} unds)"
