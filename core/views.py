from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login # as duas funções responsáveis pela autenticação: 1-authenticate - verifica o login e senha; 2- login - realiza a autenticação no sistema.
from django.contrib.auth import logout #função responsável pelo logout
from django.contrib.auth.decorators import permission_required #Definindo que o acesso à View só será feito por usuários que tiverem a permissão permissao_adm_1 definida:
from django.contrib.auth.models import Permission #Primeiro passo: Importar o objeto Permission em Views:
from django.contrib.auth.forms import UserCreationForm #Registro: UserCreationForm: é um ModelForm que já vem implementado no Django, com 3 campos para o registro de usuário: username, password1 e password2.
from .forms import  CategoriaForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Categorias, Usuario, Endereco
from .forms import UsuarioForm
from .forms import EnderecoForm
from django.shortcuts import get_list_or_404
from .forms import AddPermissionForm
from django.shortcuts import get_object_or_404
from .models import Anexos
from .forms import AnexosForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from .forms import AdicionarImagemForm
from datetime import datetime
from django.utils import timezone
from .forms import SobreOGrupoForm
from .models import SobreOGrupo
from .models import Pesquisadores
from .forms import PesquisadoresForm
from django.shortcuts import render
from .models import Anexos


# def home (resquest):
#     return render(resquest, "index.html")

def home(request):
    grupos = SobreOGrupo.objects.all()
    return render(request, 'index.html', {'grupos': grupos})


def pagina_de_sucesso (resquest):
    return render(resquest, "pagina_de_sucesso.html")
                  
def detalhe_noticia (resquest):
    return render(resquest, "detalhe_noticia.html")

def noticias (resquest):
    return render(resquest, "noticias.html")

def pesquisadores(request):
    pesquisadores = Pesquisadores.objects.all()
    return render(request, 'pesquisadores.html', {'pesquisadores': pesquisadores})

# def pesquisadores(request, pesquisador_id):
#     pesquisador = Pesquisadores.objects.get(id=pesquisador_id)
#     return render(request, 'pesquisadores.html', {'pesquisador': pesquisador})


@login_required
def perfil(request):
     # Recupere o usuário logado
    user = request.user

    # Verifique se o usuário já tem uma imagem de perfil cadastrada
    tem_imagem_perfil = bool(user.imagem)

    return render(request, 'perfil.html', {'user': user, 'tem_imagem_perfil': tem_imagem_perfil})





@login_required
def adicionar_imagem_perfil(request):
    if request.method == 'POST':
        form = AdicionarImagemForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirecionar para a página de perfil após o upload
    else:
        form = AdicionarImagemForm()
    return render(request, 'adicionar_imagem.html', {'form': form})

@login_required
def excluir_imagem_perfil(request):
    # Recupere o usuário logado
    user = request.user
    # Defina o campo "imagem" do usuário como None (ou limpe o campo)
    user.imagem = None
    user.save()
    return redirect('perfil')  # Redirecionar para a página de perfil após a exclusão

@login_required
def editar_imagem_perfil(request):
    if request.method == 'POST':
        form = AdicionarImagemForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirecionar para a página de perfil após a edição
    else:
        form = AdicionarImagemForm(instance=request.user)
    return render(request, 'editar_imagem.html', {'form': form})












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
        return render(request, 'registration/login.html')
    


@login_required
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






    """ user = Usuario.objects.create_user(
        username='Vilani01',
        email='josevilani02@email.com',
        cpf='02000300000',
        nome='Jose Vilani de Farias',
        password='admin333',
        telefone=8440054114,
        categoria = Categorias.objects.get(pk=1),
        is_superuser=False)
        
"""
def cadastro_manual(request):
    permission1 = Permission.objects.get(codename='Administrador') #Adicionando permissão ao administrador
    user = Usuario.objects.get(email='josechacon@gmail.com')
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
@login_required 
def listar_categoria(request):       
    categoria = Categorias.objects.all()
    contexto = {
        'todas_categoria': categoria
    }
    return render (request, 'categoria.html', contexto)


@login_required 
def cadastrar_categoria(request):     
    form = CategoriaForm(request.POST or None)

    if form.is_valid(): 
        form.save()
        return redirect('listar_categoria') 

    contexto = {
        'form_categoria': form
    }
    return render(request, 'categoria_cadastrar.html', contexto)


@login_required 
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


@login_required 
def remover_categoria(request, id): 
    categoria = Categorias.objects.get(pk=id) 
    categoria.delete()
    return redirect('listar_categoria')








#Endereçooo
@login_required 
def listar_endereco(request):       
    endereco = Endereco.objects.filter(usuario=request.user)
    contexto = {
        'todos_endereco': endereco
    }
    return render (request, 'endereco.html', contexto)


@login_required 
def cadastrar_endereco(request):     
    form = EnderecoForm(request.POST or None)
    if form.is_valid(): 
        endereco = form.save(commit=False)
        endereco.usuario = request.user
        endereco.save()
        return redirect('listar_endereco') 

    contexto = {
        'form_endereco': form
    }
    return render(request, 'endereco_cadastrar.html', contexto)


@login_required 
def editar_endereco(request, id): #EDITAR nome da categoria
    endereco = Endereco.objects.get(pk=id)

    form = EnderecoForm(request.POST or None, instance=endereco)

    if form.is_valid():
        form.save()
        return redirect('listar_endereco')

    contexto = {
        'form_endereco': form
    }    

    return render (request, 'endereco_cadastrar.html', contexto)


@login_required 
def remover_endereco(request, id): 
    endereco = Endereco.objects.get(pk=id) 
    endereco.delete()
    return redirect('listar_endereco')



# def teste(request, idUsuario):
#     usuario = Usuario.objects.get(id=idUsuario)
#     grupoAdmin = Group.objects.get(name='Administradores') 
#     grupoAdmin.user_set.add(usuario)
#     return redirect('add-admin')



#lista de usuarios

def user_list(request):
    usuario = Usuario.objects.all()
    context = {'usuario': usuario}
    return render(request, 'user_list.html', context)




def sucesso_add_permission(request):
    return render(request, 'sucesso_add_permission.html')



#Atribuindo permissões a usuarios

@login_required
def add_permission(request, user_id):
    usuario = get_object_or_404(Usuario, id=user_id)

    if request.method == 'POST':
        form = AddPermissionForm(request.POST)
        if form.is_valid():
            permissions = form.cleaned_data['permissions']
            usuario.user_permissions.set(permissions)
            return redirect('sucesso_add_permission')
    else:
        form = AddPermissionForm()

    context = {
        'form': form,
        'user': usuario
    }
    return render(request, 'add_permission.html', context)

















@login_required
def submeter_artigo(request):
    if request.method == 'POST':
        form = AnexosForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.usuario = request.user
            artigo.save()
            artigo.status = 'pendente'
            return redirect('pagina_de_sucesso')
    else:
        form = AnexosForm()
    return render(request, 'submeter_artigo.html', {'form': form})


@login_required
def listar_artigos(request):
    if request.user.is_superuser:
        artigos_pendentes = Anexos.objects.filter(status='pendente')
        artigos_deferidos = Anexos.objects.exclude(status='pendente').select_related('deferido_por')
    else:
        artigos_pendentes = Anexos.objects.filter(status='pendente', deferido_por=None)
        artigos_deferidos = Anexos.objects.filter(deferido_por__isnull=False).select_related('deferido_por')

    # Deixa a primeira letra do status em maiúscula para todos os artigos
    for artigo in artigos_pendentes:
        artigo.status = artigo.status.capitalize()

    for artigo in artigos_deferidos:
        artigo.status = artigo.status.capitalize()

    return render(request, 'listar_artigos.html', {'artigos_pendentes': artigos_pendentes, 'artigos_deferidos': artigos_deferidos})



@login_required
def detalhes_artigo(request, artigo_id):
    artigo = get_object_or_404(Anexos, id=artigo_id)
    return render(request, 'detalhes_artigo.html', {'artigo': artigo})



@login_required
def meus_artigos(request):
    artigos = Anexos.objects.filter(usuario=request.user)
    for artigo in artigos:
        artigo.disable_exclusao = artigo.status == "deferido"
        artigo.status = artigo.status.capitalize()
    contexto = {'artigos': artigos}
    return render(request, 'meus_artigos.html', contexto)


@login_required
def excluir_artigo(request, artigo_id):
    artigo = get_object_or_404(Anexos, id=artigo_id, usuario=request.user)
    artigo.delete()
    return redirect('meus_artigos')



from django.shortcuts import redirect, get_object_or_404

@login_required
def deferir_artigo(request, artigo_id):
    artigo = get_object_or_404(Anexos, id=artigo_id, status='pendente')
    artigo.status = 'deferido'
    artigo.deferido_por = request.user
    artigo.data_deferimento = timezone.now() 
    artigo.save()
    return redirect('listar_artigos')

@login_required
def indeferir_artigo(request, artigo_id):
    artigo = get_object_or_404(Anexos, id=artigo_id, status='pendente')
    artigo.status = 'indeferido'
    artigo.deferido_por = request.user
    artigo.data_deferimento = timezone.now()
    artigo.save()
    return redirect('listar_artigos')


#publicado automaticamente

def artigos_e_projetos(request):
    artigos_deferidos = Anexos.objects.filter(status='deferido')

    # Filtrar os resultados com base no termo de pesquisa
    query = request.GET.get('q')
    if query:
        artigos_deferidos = artigos_deferidos.filter(titulo__icontains=query) | artigos_deferidos.filter(descricao__icontains=query)

    return render(request, 'artigos_e_projetos.html', {'artigos_deferidos': artigos_deferidos})




#SOBRE O GRUPO
@login_required
def cadastrar_sobre_o_grupo(request):
    if request.method == 'POST':
        form = SobreOGrupoForm(request.POST, request.FILES)
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.usuario = request.user
            grupo.save()
            return redirect('listar_sobre_o_grupo')
    else:
        form = SobreOGrupoForm()
    return render(request, 'cadastrar_sobre_o_grupo.html', {'form': form})


def listar_sobre_o_grupo(request):
    grupos = SobreOGrupo.objects.all()
    return render(request, 'listar_sobre_o_grupo.html', {'grupos': grupos})


@login_required
def editar_sobre_o_grupo(request, grupo_id):
    grupo = get_object_or_404(SobreOGrupo, id=grupo_id)
    if request.method == 'POST':
        form = SobreOGrupoForm(request.POST, request.FILES, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('listar_sobre_o_grupo')
    else:
        form = SobreOGrupoForm(instance=grupo)
    return render(request, 'editar_sobre_o_grupo.html', {'form': form})

@login_required
def excluir_sobre_o_grupo(request, grupo_id):
    grupo = get_object_or_404(SobreOGrupo, id=grupo_id)
    grupo.delete()
    return redirect('listar_sobre_o_grupo')


def sobre(request):
    grupos = SobreOGrupo.objects.all()
    return render(request, 'sobre.html', {'grupos': grupos})


@login_required
def cadastrar_pesquisador(request):
    if request.method == 'POST':
        form = PesquisadoresForm(request.POST, request.FILES)
        if form.is_valid():
            pesquisador = form.save(commit=False)
            # Defina o usuário do pesquisador com base no usuário logado
            pesquisador.usuario = request.user
            pesquisador.save()
            return redirect('listar_pesquisadores')  # Redirecionar para a página de sucesso após o cadastro
    else:
        form = PesquisadoresForm()
    return render(request, 'cadastrar_pesquisador.html', {'form': form})


def listar_pesquisadores(request):
    pesquisadores = Pesquisadores.objects.all()
    return render(request, 'listar_pesquisadores.html', {'pesquisadores': pesquisadores})

@login_required
def editar_pesquisador(request, pesquisador_id):
    pesquisador = get_object_or_404(Pesquisadores, pk=pesquisador_id)
    if request.method == 'POST':
        form = PesquisadoresForm(request.POST, request.FILES, instance=pesquisador)
        if form.is_valid():
            form.save()
            # Redirecionar para a página de lista de pesquisadores após a edição
            return redirect('listar_pesquisadores')
    else:
        form = PesquisadoresForm(instance=pesquisador)
    return render(request, 'editar_pesquisador.html', {'form': form})


@login_required
def excluir_pesquisador(request, pesquisador_id):
    pesquisador = get_object_or_404(Pesquisadores, id=pesquisador_id)
    pesquisador.delete()
    return redirect('listar_pesquisadores')