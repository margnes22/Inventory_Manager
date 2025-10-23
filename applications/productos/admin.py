from django.contrib import admin

# Register your models here.

from .models import Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre',)
    list_filter = ('fecha_creacion',)
    ordering = ('-fecha_creacion',)
    date_hierarchy = 'fecha_creacion'
