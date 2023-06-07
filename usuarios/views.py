from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def cadastro(request):
    #Se não tiver o forms preenchido
    if request.method == "GET":
        return render(request, 'cadastro.html')
    
    #Se tiver o forms preenchido
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        #Filtra pra saber se já existe um usuário com o username indicado
        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse nome de usuário')
        
        novoUser = User.objects.create_user(username=username, email=email, password=senha)
        novoUser.save()

        
        return HttpResponse('Usuário cadastrado com sucesso.')

def login(request):
    return render(request, 'login.html')