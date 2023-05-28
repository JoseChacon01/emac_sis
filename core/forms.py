from dataclasses import fields
from .models import Usuario
from .models import Categorias
from .models import Endereco
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