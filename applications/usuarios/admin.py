from django.contrib import admin
from .models import Usuario
# Register your models here.

@admin.register(Usuario)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'rol')  # 👈 Campos visibles en la tabla
    search_fields = ('nombre', 'apellido', 'email')                    # 🔍 Campos para buscar
    list_filter = ('rol',)  