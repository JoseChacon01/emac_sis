from dataclasses import fields
from .models import Usuario
from .models import Categorias
from .models import Cidade
from .models import Bairro
from .models import Pais_Regiao
from .models import Endereco
from .models import Noticias
from .models import Cadastros
from .models import Eventos


from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm





class CategoriaForm(ModelForm):
    class Meta:
        model = Categorias
        fields = ['nome']   

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'email', 'nome', 'telefone', 'cpf', 'categoria']          




class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = ['pais_nac', 'cep', 'estado_nac', 'cidade_nac', 'bairro_nac', 'endereco', 'numero', 'complemento']




class CadastrosForm(ModelForm):
    class Meta:
        model = Cadastros
        fields = ['data_cadastro', 'titulo', 'descricao', 'tipo_do_trabalho'] 

class NoticiasForm(ModelForm):
    class Meta:
        model = Noticias
        fields = ['fonte', 'publico_alvo', 'data_validacao_noticia','foto','urlLink', 'arquivo_pdf'] 

class EventosForm(ModelForm):
    class Meta:
        model = Eventos
        fields = ['formato', 'local', 'data_evento','foto','urlLink', 'arquivo_pdf'] 


