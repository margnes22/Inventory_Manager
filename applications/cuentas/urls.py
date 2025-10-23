from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
