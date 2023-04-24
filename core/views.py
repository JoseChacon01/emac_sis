from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login # as duas funções responsáveis pela autenticação: 1-authenticate - verifica o login e senha; 2- login - realiza a autenticação no sistema.
from django.contrib.auth import logout #função responsável pelo logout
from django.contrib.auth.decorators import permission_required #Definindo que o acesso à View só será feito por usuários que tiverem a permissão permissao_adm_1 definida:
from django.contrib.auth.models import Permission #Primeiro passo: Importar o objeto Permission em Views:
from django.contrib.auth.forms import UserCreationForm #Registro: UserCreationForm: é um ModelForm que já vem implementado no Django, com 3 campos para o registro de usuário: username, password1 e password2.
from .forms import  CategoriaForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Categorias, Usuario
from .forms import UsuarioForm
#from .forms import UsuarioForm


def detalhe_noticia (resquest):
    return render(resquest, "detalhe_noticia.html")

def noticias (resquest):
    return render(resquest, "noticias.html")

def pesquisadores (resquest):
    return render(resquest, "pesquisadores.html")

@login_required
def perfil(request):
    return render(request, 'perfil.html')

def home (resquest):
    return render(resquest, "index.html")



def autenticacao(request):
    '''
    se o usuário digitou algo no formulário e clicou em enviar, o if 
    será verdadeiro, caso contrário, será uma requisição GET e entrara no else.
    -
    '''
    if request.POST:
       usuario = request.POST['usuario']
       senha = request.POST['senha']
       user = authenticate(request, username=usuario, password=senha)
       if user is not None:
        login(request, user)
        #messages.success(request, 'Bem-vindo(a)') #corrigir
        return redirect('perfil')
       else:
        return redirect('login') 
    else:
        return render(request, 'registration\login.html') 
    



def pagina_usuarios(request, categoria_url): 
    #Listar usuarios do BD
    if categoria_url == 'todos':
        todos_usuarios = Usuario.objects.all()
    else:
        todos_usuarios = Usuario.objects.filter(categoria=categoria_url)
    
    todas_categorias = Categorias.objects.all()

    contexto = {
        'todos_usuarios' : todos_usuarios,
        'todas_categorias': todas_categorias,
        'categoria_selecionada': categoria_url
    }
    return render(request, 'usuarios.html', contexto) 







def cadastro_manual(request):
    

    user = Usuario.objects.create_user(
        username='Vilani01',
        email='josevilani02@email.com',
        cpf='02000300000',
        nome='Jose Vilani de Farias',
        password='admin333',
        telefone=8440054114,
        categoria = Categorias.objects.get(pk=1),
        is_superuser=False)
        

    permission1 = Permission.objects.get(codename='Administrador')
    user.user_permissions.add(permission1)


    user.save()
    return redirect('home')   






def registro(request):
    form = UsuarioForm(request.POST or None) #Inplemantando o registro utilizando a class criada emm 'forms.py'
    if form.is_valid(): #Ao realizar o registro, automaticamente o usuário será redirecionado para a página de login:
        form.save()
        return redirect('login')
    contexto = {
        'form': form
        }
    return render(request, 'registro.html', contexto)





def desconectar(request):
    logout(request)
    return render(request, 'index.html')     






def dados(request, id):
    user = Usuario.objects.get(pk=id)
    form = UsuarioForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()   
        return redirect('perfil')
    contexto = {
        'form': form
    }    
    return render(request, 'registro.html', contexto)






#Categoria
def listar_categoria(request):       
    categoria = Categorias.objects.all()
    contexto = {
        'todas_categoria': categoria
    }
    return render (request, 'categoria.html', contexto)



def cadastrar_categoria(request):     
    form = CategoriaForm(request.POST or None)

    if form.is_valid(): 
        form.save()
        return redirect('listar_categoria') 

    contexto = {
        'form_categoria': form
    }
    return render(request, 'categoria_cadastrar.html', contexto)



def editar_categoria(request, id): #EDITAR nome da categoria
    categoria = Categorias.objects.get(pk=id)

    form = CategoriaForm(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('listar_categoria')

    contexto = {
        'form_categoria': form
    }    

    return render (request, 'categoria_cadastrar.html', contexto)



def remover_categoria(request, id): 
    categoria = Categorias.objects.get(pk=id) 
    categoria.delete()
    return redirect('listar_categoria')