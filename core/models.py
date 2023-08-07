from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser #Padrão



class Categorias(models.Model):
      nome = models.CharField('Nome', max_length=100) #Professor, pesquisador, aluno e administrador
    
      def __str__(self):
       return self.nome 




class SobreOGrupo(models.Model):
     descricao_grupo = models.CharField('Descricao_grupo', max_length=500)
     imagem_grupo = models.ImageField('Imagem_grupo')



class Usuario(AbstractUser):
    nome = models.CharField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=11, unique=True) #unique não permite que tenha 2 cadastros com o memso dado, nesse caso, o CPF.
    telefone = models.IntegerField('Telefone')
    imagem = models.ImageField('Imagem', null=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)

    USERNAME_FIELD = 'cpf' 

    class Meta:  
         permissions = [
             ("Administrador", "Utilização das funções gerais do sistema")
         ]


class Pesquisadores(models.Model):
     curriculo = models.CharField('Curriculo', max_length=150)
     projetos_vinculados = models.CharField('Projetos_vinculados', max_length=200)
     artigos_vinculados = models.CharField('Artigos_vinculados', max_length=200)
     biografia = models.CharField('Biografia', max_length=300)
     imagem_pesquisador = models.ImageField('Imagem_Pesquisador', null=True)
     sobreogrupo = models.ForeignKey(SobreOGrupo, on_delete=models.PROTECT)
     usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)


class Pais_Regiao(models.Model):          
     pais_regiao = models.CharField('Pais_regiao', max_length=120)


class Estado(models.Model):
     estado = models.CharField('Estado', max_length=120)
     pais_regiao = models.ForeignKey(Pais_Regiao, on_delete=models.PROTECT)


class Cidade(models.Model):
     cidade = models.CharField('Cidade', max_length=120)
     estado = models.ForeignKey(Estado, on_delete=models.PROTECT)  

class Bairro(models.Model):
     bairro = models.CharField('Bairro', max_length=80)      
     cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT) 

class Endereco(models.Model):
    pais_nac = models.CharField('Pais_nac', max_length=120)
    cep = models.IntegerField('CEP')
    estado_nac = models.CharField('Estado_nac', max_length=120)
    cidade_nac = models.CharField('Cidade_nac', max_length=120)
    bairro_nac = models.CharField('Bairro_nac', max_length=80)  
    cep = models.IntegerField('CEP')
    endereco = models.CharField('endereco', max_length=120)
    numero = models.IntegerField('Numero')
    complemento = models.CharField('Complemento', max_length=200, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    



class Cadastros(models.Model):
     data_cadastro = models.DateField('Data_Cadastro')
     titulo = models.CharField('Titulo', max_length=50)
     descricao = models.CharField('Descricao', max_length=300)
     tipo_do_trabalho = models.CharField('Tipo_trabalho', max_length=50)
     usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class Noticias(models.Model):
     fonte = models.CharField('Fonte', max_length=150)
     publico_alvo = models.CharField ('Publico_alvo', max_length=150)
     data_validacao_noticia = models.DateField('Data_validacao_noticia')
     cadastro = models.ForeignKey(Cadastros, on_delete=models.PROTECT)
     urlLink = models.URLField('UrlLink', max_length=200, default='')
     arquivo_pdf = models.FileField(upload_to='pdfs/', default='default.pdf',null=True)
     foto = models.ImageField(upload_to='noticias', null=True)


class Eventos(models.Model):
     formato = models.CharField('Formato', max_length=50)
     local = models.CharField('Local', max_length=100)
     data_evento = models.DateField('Data_evento')
     foto = models.ImageField(upload_to='eventos', null=True)
     urlLink = models.URLField('UrlLink', max_length=200, default='')
     arquivo_pdf = models.FileField(upload_to='pdfs/', default='default.pdf')
     cadastro = models.ForeignKey(Cadastros, on_delete=models.PROTECT)




class Projetos(models.Model):
     cadastro = models.ForeignKey(Cadastros, on_delete=models.PROTECT)
     pesquisadores = models.ForeignKey(Pesquisadores, on_delete=models.PROTECT)
     



class Instituicoes(models.Model):
     nome_instituicao = models.CharField('Nome_instituicao', max_length=200)


class Editoras(models.Model):
     nome_editora = models.CharField('Nome_editora', max_length=100)




class Anexos(models.Model):
     anexos = models.BinaryField('Anexos')
     descricao = models.CharField('Descricao', max_length=350)
     nome_periodico = models.CharField('Nome_periodico', max_length=50)
     resumo = models.CharField('Resumo', max_length=400)
     data_validacao_anexo = models.DateField('Data_validacao_anexo')
     issn = models.CharField('ISSN', max_length=70)
     cadastro = models.ForeignKey(Cadastros, on_delete=models.PROTECT)
     editoras = models.ForeignKey(Editoras, on_delete=models.PROTECT)
     instituicoes = models.ForeignKey(Instituicoes, on_delete=models.PROTECT)