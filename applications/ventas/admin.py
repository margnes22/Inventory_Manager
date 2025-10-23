from django.contrib import admin

# Register your models here.
from .models import Venta

admin.site.register(Venta)

class VentaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'precio_unitario', 'total', 'fecha_venta', 'vendedor', 'cliente')
    search_fields = ('producto__nombre', 'vendedor__username', 'cliente')
    list_filter = ('fecha_venta', 'vendedor')
