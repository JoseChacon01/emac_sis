from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser #Padrão
from datetime import date


class Categorias(models.Model):
      nome = models.CharField('Nome', max_length=100) #Professor, pesquisador, aluno e administrador
    
      def __str__(self):
       return self.nome 





class Usuario(AbstractUser):
    nome = models.CharField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=11, unique=True) #unique não permite que tenha 2 cadastros com o memso dado, nesse caso, o CPF.
    telefone = models.IntegerField('Telefone', null=True)
    imagem = models.ImageField('Imagem', null=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT, null=True)
    username = models.CharField(null=True, max_length=50)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['username']

    class Meta:  
         permissions = [
             ("Administrador", "Utilização das funções gerais do sistema")
         ]




class SobreOGrupo(models.Model):
     descricao_grupo = models.CharField('Descricao_grupo', max_length=2500)
     imagem_grupo = models.ImageField('Imagem_grupo')
     usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, default=12)



class Pesquisadores(models.Model):
     nome = models.CharField('Nome', max_length=200, default='')
     urlcurriculo = models.URLField('UrlCurriculo', max_length=200, default='')
     #projetos_vinculados = models.CharField('Projetos_vinculados', max_length=200)
     #artigos_vinculados = models.CharField('Artigos_vinculados', max_length=200)
     biografia = models.CharField('Biografia', max_length=600)
     imagem_pesquisador = models.ImageField('Imagem_Pesquisador', null=True)
     #sobreogrupo = models.ForeignKey(SobreOGrupo, on_delete=models.PROTECT)
     usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)




class Endereco(models.Model):
    pais_nac = models.CharField('Pais_nac', max_length=120)
    cep = models.IntegerField('CEP')
    estado_nac = models.CharField('Estado_nac', max_length=120)
    cidade_nac = models.CharField('Cidade_nac', max_length=120)
    bairro_nac = models.CharField('Bairro_nac', max_length=80)  
    endereco = models.CharField('endereco', max_length=120)
    numero = models.IntegerField('Numero')
    complemento = models.CharField('Complemento', max_length=200, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    



class Cadastros(models.Model):
     data_cadastro = models.DateField('Data_Cadastro', default=date.today)
     titulo = models.CharField('Titulo', max_length=170)
     descricao = models.CharField('Descricao', max_length=1000)
     tipo_do_trabalho = models.CharField('Tipo_trabalho', max_length=50, default='')
     usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class Noticias(models.Model):
     fonte = models.CharField('Fonte', max_length=350)
     publico_alvo = models.CharField ('Publico_alvo', max_length=350)
     cadastro = models.ForeignKey(Cadastros, on_delete=models.PROTECT)
     urlLink = models.URLField('UrlLink', max_length=300, default='')
     arquivo_pdf = models.FileField(upload_to='pdfs/', default='default.pdf',null=True)
     foto = models.ImageField(upload_to='noticias', null=True)


class Eventos(models.Model):
     formato = models.CharField('Formato', max_length=100)
     local = models.CharField('Local', max_length=200)
     data_evento = models.DateField('Data_evento')
     foto = models.ImageField(upload_to='eventos', null=True)
     urlLink = models.URLField('UrlLink', max_length=250, default='')
     arquivo_pdf = models.FileField(upload_to='pdfs/', default='default.pdf',null=True)
     cadastro = models.ForeignKey(Cadastros, on_delete=models.PROTECT)




# class Projetos(models.Model):
#      cadastro = models.ForeignKey(Cadastros, on_delete=models.PROTECT)
#      pesquisadores = models.ForeignKey(Pesquisadores, on_delete=models.PROTECT)
     

class Anexos(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Avaliação Pendente'),
        ('deferido', 'Deferido'),
        ('indeferido', 'Indeferido'),
    )

    data_cadastro = models.DateField('Data_Cadastro', default=date.today)
    titulo = models.CharField('Título', max_length=200)
    descricao = models.CharField('Descrição', max_length=900)
    nome_periodico = models.CharField('Nome do Periódico', max_length=50)
    arquivo_pdf = models.FileField(upload_to='pdfs/', default='default.pdf')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    deferido_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='artigos_deferidos')
    data_deferimento = models.DateTimeField(blank=True, null=True)
    issn = models.CharField('ISSN', max_length=70)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=12)
    nome_editora = models.CharField('Nome da Editora', max_length=100)
    nome_instituicao = models.CharField('Nome da Instituição', max_length=200)

    @staticmethod
    def get_default_pdf():
        return 'default.pdf'