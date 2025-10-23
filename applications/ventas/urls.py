from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('', views.lista_ventas, name='lista_ventas'),
    path('nueva/', views.nueva_venta, name='nueva_venta'),
    path('editar/<int:venta_id>/', views.editar_venta, name='editar_venta'),
    path('eliminar/<int:venta_id>/', views.eliminar_venta, name='eliminar_venta'),  # ✅ esta línea
]
