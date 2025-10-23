from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm

@login_required
def lista_productos(request):
    productos = Producto.objects.all().order_by('-fecha_creacion')
    return render(request, 'productos_lista.html', {'productos': productos})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productos:lista_productos')  # <-- ya usa namespace:name correcto
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form, 'titulo': 'Nuevo producto'})

@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos:lista_productos')  # <-- corregido
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_form.html', {'form': form, 'titulo': 'Editar Producto'})

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos:lista_productos')  # <-- corregido
    return render(request, 'producto_confirmar_eliminar.html', {'producto': producto})
