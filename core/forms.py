from dataclasses import fields
from .models import Usuario
from .models import Categorias
from .models import Endereco
from .models import Noticias
from .models import Cadastros
from .models import Eventos


from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User, Permission
from .models import Anexos
from django import forms
from .models import SobreOGrupo
from .models import Pesquisadores





class CategoriaForm(ModelForm):
    class Meta:
        model = Categorias
        fields = ['nome']   
#
class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True) 
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'email', 'nome', 'telefone', 'cpf', 'categoria']          



class AdicionarImagemForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['imagem']

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = ['pais_nac', 'cep', 'estado_nac', 'cidade_nac', 'bairro_nac', 'endereco', 'numero', 'complemento']




class CadastrosForm(ModelForm):
    class Meta:
        model = Cadastros
        fields = ['titulo', 'descricao', 'tipo_do_trabalho'] 

class NoticiasForm(ModelForm):
    class Meta:
        model = Noticias
        fields = ['fonte', 'publico_alvo', 'foto','urlLink', 'arquivo_pdf'] 

class EventosForm(ModelForm):
    class Meta:
        model = Eventos
        fields = ['formato', 'local', 'data_evento','foto','urlLink', 'arquivo_pdf'] 


class AddPermissionForm(forms.Form):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )



class SobreOGrupoForm(forms.ModelForm):
    class Meta:
        model = SobreOGrupo
        fields = ['descricao_grupo', 'imagem_grupo']
        


class AnexosForm(forms.ModelForm):
    class Meta:
        model = Anexos
        fields = ['titulo', 'descricao', 'nome_periodico', 'arquivo_pdf', 'issn', 'nome_editora', 'nome_instituicao', 'motivo_indeferimento']
        labels = { #rótulos personalizados
            'motivo_indeferimento': 'Motivo do Indeferimento'
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].widget.attrs.update({'class': 'input_box', 'required': 'required'})


# class MotivoIndeferimentoForm(forms.ModelForm):
#     class Meta:
#         model = Anexos
#         fields = ['motivo_indeferimento']
#         labels = { #rótulos personalizados
#             'motivo_indeferimento': 'Motivo do Indeferimento'
#         }


class PesquisadoresForm(forms.ModelForm):
    class Meta:
        model = Pesquisadores
        fields = ['nome', 'urlcurriculo', 'biografia', 'imagem_pesquisador']
