from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('nuevo/', views.crear_producto, name='producto_crear'),
    path('editar/<int:id>/', views.editar_producto, name='producto_editar'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='producto_eliminar'),
]
