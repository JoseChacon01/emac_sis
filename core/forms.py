from dataclasses import fields
from .models import Usuario
from .models import Categorias
from .models import Endereco
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User, Permission
from .models import Anexos
from django import forms



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


class AddPermissionForm(forms.Form):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )






class AnexosForm(forms.ModelForm):
    class Meta:
        model = Anexos
        fields = ['titulo', 'descricao', 'nome_periodico', 'arquivo_pdf', 'issn', 'nome_editora', 'nome_instituicao']
