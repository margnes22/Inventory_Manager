from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Venta
from .forms import VentaForm

@login_required
def lista_ventas(request):
    ventas = Venta.objects.all().order_by('-fecha_venta')
    return render(request, 'lista_ventas.html', {'ventas': ventas})

@login_required
def nueva_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.vendedor = request.user
            venta.save()
            messages.success(request, '✅ Venta registrada correctamente.')
            return redirect('ventas:lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'nueva_venta.html', {'form': form})

@login_required
def editar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)

    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Venta actualizada correctamente.')
            return redirect('ventas:lista_ventas')
    else:
        form = VentaForm(instance=venta)

    return render(request, 'editar_venta.html', {'form': form, 'venta': venta})

@login_required
def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    if request.method == 'POST':
        venta.delete()
        messages.success(request, '🗑️ Venta eliminada correctamente.')
        return redirect('ventas:lista_ventas')
    return render(request, 'confirmar_eliminar_venta.html', {'venta': venta})