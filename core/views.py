from django.shortcuts import redirect, render ,get_object_or_404
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
from .models import Categorias, Usuario, Endereco, Noticias, Cadastros, Eventos
from .forms import UsuarioForm
from .forms import EnderecoForm
from .forms import NoticiasForm , CadastrosForm
from .forms import EventosForm








from django.http import HttpResponse
from django.shortcuts import get_object_or_404

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


def cadastro_noticias1 (resquest):
    return render(resquest, "cadastro_noticias1.html")



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
    user = Usuario.objects.get(email='josevilani02@email.com')
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



#views referente as rotas da noticias

def cadastro_noticias(request):
    if request.method == 'POST':
        form1 = CadastrosForm(request.POST)
        form2 = NoticiasForm(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            cadastro = form1.save(commit=False)  # Não salva ainda no banco de dados
            cadastro.usuario = request.user  # Associar o cadastro ao usuário logado
            cadastro.save()  # Agora salva no banco de dados

            noticias = form2.save(commit=False)  # Não salva ainda no banco de dados
            noticias.cadastro = cadastro  # Vinculando o cadastro ao objeto noticias
            noticias.save()  # Salvando agora no banco de dados com a chave estrangeira preenchida

            # Redirecionar para uma página de sucesso ou qualquer outra página desejada
            return redirect('listar_noticia')

    else:
        form1 = CadastrosForm()
        form2 = NoticiasForm()

    return render(request, 'cadastro_noticias.html', {'form1': form1, 'form2': form2})


class DadosCompletos:
    def __init__(self, cadastro, noticia):
        self.cadastro_id = noticia.cadastro_id
        self.titulo = cadastro.titulo
        self.descricao = cadastro.descricao
        self.data_cadastro = cadastro.data_cadastro
        self.tipo_do_trabalho = cadastro.tipo_do_trabalho   
        self.data_validacao_noticia = noticia.data_validacao_noticia
        self.fonte = noticia.fonte
        self.publico_alvo = noticia.publico_alvo
        self.foto = noticia.foto
        self.urlLink = noticia.urlLink
        self.arquivo_pdf = noticia.arquivo_pdf


        
        # Adicione mais campos conforme necessário


def noticias_listar(request):
    cadastros = Cadastros.objects.all()
    
    dados_completos = []

    for cadastro in cadastros:
        try:
            noticia = Noticias.objects.get(cadastro=cadastro)
            dados = DadosCompletos(cadastro, noticia)
            dados_completos.append(dados)
        except Noticias.DoesNotExist:
            pass

    return render(request, 'noticias.html', {'dados_completos': dados_completos})


def listar_noticia(request):
    cadastros = Cadastros.objects.all()
    
    dados_completos = []

    for cadastro in cadastros:
        try:
            noticia = Noticias.objects.get(cadastro=cadastro)
            dados = DadosCompletos(cadastro, noticia)
            dados_completos.append(dados)
        except Noticias.DoesNotExist:
            pass

    return render(request, 'listar_noticia.html', {'dados_completos': dados_completos})


def noticia_remover(request, cadastro_id): 
    cadastro = get_object_or_404(Cadastros, pk=cadastro_id)
    noticias = Noticias.objects.filter(cadastro=cadastro)

    # Exclui todas as notícias associadas ao cadastro
    for noticia in noticias:
        noticia.delete()

    # Exclui o próprio cadastro
    cadastro.delete()
    return redirect('listar_noticia')

def noticia_editar(request, cadastro_id):
    cadastro = Cadastros.objects.get(pk=cadastro_id)

    try:
        noticia = Noticias.objects.get(cadastro=cadastro)
    except Noticias.DoesNotExist:
        noticia = None

    form1 = CadastrosForm(instance=cadastro)
    form2 = NoticiasForm(instance=noticia)

    if request.method == 'POST':
        form1 = CadastrosForm(request.POST, instance=cadastro)
        form2 = NoticiasForm(request.POST, request.FILES, instance=noticia)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()    
            return redirect('listar_noticia')

    return render(request, 'cadastro_noticias.html', {'form1': form1, 'form2': form2})



def detalhe_noticia(request, cadastro_id):
    cadastro = get_object_or_404(Cadastros, pk=cadastro_id)
    try:
        noticia = Noticias.objects.get(cadastro=cadastro)
    except Noticias.DoesNotExist:
        noticia = None

    if noticia:
        dados = DadosCompletos(cadastro, noticia)
        return render(request, 'detalhe_noticia.html', {'dados': dados})
    else:
        return render(request, 'noticia_nao_encontrada.html')


#views referente as rotas de eventos

def cadastro_evento(request):
    if request.method == 'POST':
        form1 = CadastrosForm(request.POST)
        form2 = EventosForm(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            cadastro = form1.save(commit=False)  # Não salva ainda no banco de dados
            cadastro.usuario = request.user  # Associar o cadastro ao usuário logado
            cadastro.save()  # Agora salva no banco de dados

            eventos = form2.save(commit=False)  # Não salva ainda no banco de dados
            eventos.cadastro = cadastro  # Vinculando o cadastro ao objeto noticias
            eventos.save()  # Salvando agora no banco de dados com a chave estrangeira preenchida

            # Redirecionar para uma página de sucesso ou qualquer outra página desejada
            return redirect('listar_evento')

    else:
        form1 = CadastrosForm()
        form2 = EventosForm()

    return render(request, 'cadastro_evento.html', {'form1': form1, 'form2': form2})





class DadosCompletos1:
    def __init__(self, cadastro, evento):
        self.cadastro_id = evento.cadastro_id
        self.titulo = cadastro.titulo
        self.descricao = cadastro.descricao
        self.data_cadastro = cadastro.data_cadastro
        self.tipo_do_trabalho = cadastro.tipo_do_trabalho   
        self.formato = evento.formato
        self.local = evento.local
        self.data_evento = evento.data_evento
        self.foto = evento.foto
        self.urlLink = evento.urlLink
        self.arquivo_pdf = evento.arquivo_pdf


        
        # Adicione mais campos conforme necessário


def eventos_listar(request):
    cadastros = Cadastros.objects.all()
    
    dados_completos = []

    for cadastro in cadastros:
        try:
            noticia = Eventos.objects.get(cadastro=cadastro)
            dados = DadosCompletos1(cadastro, noticia)
            dados_completos.append(dados)
        except Eventos.DoesNotExist:
            pass

    return render(request, 'eventos.html', {'dados_completos': dados_completos})


def listar_evento(request):
    cadastros = Cadastros.objects.all()
    
    dados_completos1 = []

    for cadastro in cadastros:
        try:
            evento = Eventos.objects.get(cadastro=cadastro)
            dados = DadosCompletos1(cadastro, evento)
            dados_completos1.append(dados)
        except Eventos.DoesNotExist:
            pass

    return render(request, 'listar_evento.html', {'dados_completos': dados_completos1})



def evento_remover(request, cadastro_id): 
    cadastro = get_object_or_404(Cadastros, pk=cadastro_id)
    eventos = Eventos.objects.filter(cadastro=cadastro)

    # Exclui todas as notícias associadas ao cadastro
    for evento in eventos:
        evento.delete()

    # Exclui o próprio cadastro
    cadastro.delete()
    return redirect('listar_evento')

def evento_editar(request, cadastro_id):
    cadastro = Cadastros.objects.get(pk=cadastro_id)

    try:
        evento = Eventos.objects.get(cadastro=cadastro)
    except Eventos.DoesNotExist:
        evento = None

    form1 = CadastrosForm(instance=cadastro)
    form2 = EventosForm(instance=evento)

    if request.method == 'POST':
        form1 = CadastrosForm(request.POST, instance=cadastro)
        form2 = EventosForm(request.POST, request.FILES, instance=evento)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()    
            return redirect('listar_evento')

    return render(request, 'cadastro_evento.html', {'form1': form1, 'form2': form2})



def detalhe_evento(request, cadastro_id):
    cadastro = get_object_or_404(Cadastros, pk=cadastro_id)
    try:
        evento = Eventos.objects.get(cadastro=cadastro)
    except Eventos.DoesNotExist:
        evento = None

    if evento:
        dados = DadosCompletos1(cadastro, evento)
        return render(request, 'detalhe_evento.html', {'dados': dados})
    else:
        return render(request, 'evento_nao_encontrado.html')

