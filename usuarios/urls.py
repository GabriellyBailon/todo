from django.urls import path
from usuarios.views import login, cadastro, logout, redefinir_senha

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('redefinir_senha', redefinir_senha, name='redefinir_senha')
]