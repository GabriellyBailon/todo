from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms, RedefinirSenhaForm, RedefinirPermissao
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login(request):
    form = LoginForms()

    # Caso os campos tenham sido preenchidos, a informação deve ser registrada
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            # Primeiro, é necessário verificar se o nome de usuário inserido existe. Só é possível
            # fazer login com um usuário existente
            nome = form["nome_login"].value()
            senha = form["senha"].value()

            # Autenticação do usuário
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome} logado com sucesso')
                return redirect('./')
            else:
                messages.error(request, 'Não foi possível fazer login. Usuário ou senha errados.')
                return redirect('login')

    return render(request, 'usuarios/login.html', {"form":form})

def cadastro(request):
    form = CadastroForms()

    # Caso os campos tenham sido preenchidos, a informação deve ser registrada
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            # No cadastro é necessário verificar se a senha 1 é igual a senha 2 (A senha de confirmação)
            if form["senha_1"].value() != form["senha_2"].value():
                messages.error(request, "Senhas inseridas não são iguais")
                return redirect('cadastro')
            
            # Após validar as senhas, obtém-se os dados do formulário
            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_1"].value()

            # Verifica se já existe um usuário no banco de dados com esse nome de usuário
            # Se existir, o usuário não pode ser criado
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existe')
                return redirect('cadastro')
            
            # Se não, o usuário pode ser criado e salvo
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso')
            return redirect('login')

        
    return render(request, 'usuarios/cadastro.html', {"form":form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso.')
    return redirect('login')

@login_required(login_url='cadastro')
def redefinir_senha(request): 
    form = RedefinirSenhaForm()

    if request.method == 'POST':

        form = RedefinirSenhaForm(request.POST)

        usuario = request.user
        senha_atual = form['senha_atual'].value()
        nova_senha = form['nova_senha1'].value()
        # Verifica se a senha atual inserida está correta
        if not usuario.check_password(senha_atual):
            messages.error(request, 'Senha atual incorreta. Por favor, tente novamente.')
            return render(request, 'usuarios/redefinir.html')
        # Altera senha
        usuario.set_password(nova_senha)
        usuario.save()

        messages.success(request, "Senha alterada com sucesso.")
        return render(request, 'usuarios/login.html', {"form":form})
        
        
    return render(request, 'usuarios/redefinir.html', {"form":form})

@login_required(login_url='cadastro')
def alterar_permissao(request):
    form = RedefinirPermissao()

    if request.method == 'POST':

        form = RedefinirPermissao(request.POST)
        usuario = form['usuario'].value()

        try:
            usuario = User.objects.get(username=usuario)
        except:
            messages.error(request, f"Usuário {usuario} não existe.")
            return render(request, 'usuarios/permissoes.html', {'form':form})
        
        permissao_desejada = form['permissao'].value()
        
        if permissao_desejada == '1':
            if usuario.is_staff:
                messages.error(request, f"O usuário {usuario} já é administrador")
                return render(request, 'usuarios/permissoes.html',{'form':form})
            else:
                usuario.is_staff = 1
                usuario.save()
                messages.success(request, f'O usuário {usuario} agora é administrador.')
                return render(request, 'usuarios/permissoes.html', {'form':form})
        else:
            if not usuario.is_staff:
                messages.error(request, f"Usuário {usuario} já é comum")
                return render(request, 'usuarios/permissoes.html', {'form':form})
            else:
                usuario.is_staff = 0
                usuario.save()
                messages.success(request, f'O usuário {usuario} agora é comum')
                return render(request, 'usuarios/permissoes.html', {'form':form})

    return render(request, 'usuarios/permissoes.html', {'form':form})

