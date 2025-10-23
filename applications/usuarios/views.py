from django.shortcuts import render, redirect, get_object_or_404
from applications.cuentas.models import Usuario
from .forms import UsuarioForm  # Asegúrate de crear este formulario en forms.py

# Mostrar lista de usuarios
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista.html', {'usuarios': usuarios})

# Crear nuevo usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'formulario.html', {'form': form})

# Editar usuario existente
def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'formulario.html', {'form': form})

# Eliminar usuario
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'confirmar_eliminacion.html', {'usuario': usuario})
