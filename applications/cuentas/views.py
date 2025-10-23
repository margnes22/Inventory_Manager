from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistroForm, LoginForm
from applications.cuentas.models import Usuario
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token



def home(request):
    return render(request, 'home.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

def ayuda(request):
    return render(request, 'ayuda.html')

def contactanos(request):
    return render(request, 'contactanos.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])  # Encripta la contraseña
            usuario.save()
            messages.success(request, 'Cuenta creada correctamente.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


def login_usuario(request):
    get_token(request)  # 🔹 Fuerza la creación del token CSRF antes de renderizar

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, f'Bienvenido {username}')
                return redirect('dashboard')
            else:
                messages.error(request, 'Credenciales inválidas')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_usuario(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    # Si quieres enviar datos reales, prepara contexto aquí.
    context = {
        'ganancias': "7.852.000",
        'pedidos_data': [250, 400, 350, 500, 450, 600, 550],  # ejemplo
    }
    return render(request, 'dashboard.html', context)
