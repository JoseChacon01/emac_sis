"""
URL configuration for emac_sis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *
from core.views import add_permission

from django.views.static import serve
from django.conf import settings

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('perfil/', perfil, name='perfil'),
    path('cadastro_manual/', cadastro_manual),
    path('registro/', registro, name='registro'),
    path('pagina_usuarios/<str:categoria_url>/', pagina_usuarios, name='pagina_usuarios'), 
    path('dados/<int:id>/', dados, name='dados'),

    path('pesquisadores/', pesquisadores, name='pesquisadores'),


    path('noticias/', noticias, name='noticias'),
    path('detalhe_noticia/', detalhe_noticia, name='detalhe_noticia'),


    path('login/', autenticacao, name='login'), 
    path('logout/', desconectar, name='logout'),



    path('categoria/', listar_categoria, name='listar_categoria'),#Categoria
    path('categoria_cadastrar/', cadastrar_categoria, name='cadastrar_categoria'),
    path('categoria_editar/<int:id>/', editar_categoria, name='editar_categoria'),
    path('categoria_remover/<int:id>/', remover_categoria, name='remover_categoria'),


    path('endereco/', listar_endereco, name='listar_endereco'),#Endereço
    path('endereco_cadastrar/', cadastrar_endereco, name='cadastrar_endereco'),
    path('endereco_editar/<int:id>/', editar_endereco, name='editar_endereco'),
    path('endereco_remover/<int:id>/', remover_endereco, name='remover_endereco'),


    #Add the urls patterns :
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
 
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
 
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
 
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),



    path('add_permission/<int:user_id>/', add_permission, name='add_permission'),
    
    path('user_list/', user_list, name='user_list'),



    # URL para adicionar a imagem de perfil
    path('adicionar_imagem/', adicionar_imagem_perfil, name='adicionar_imagem'),
    # URL para excluir a imagem de perfil
    path('excluir_imagem/', excluir_imagem_perfil, name='excluir_imagem'),
    # URL para editar/mudar a imagem de perfil
    path('editar_imagem/', editar_imagem_perfil, name='editar_imagem'),


    

    path('submeter-artigo/', submeter_artigo, name='submeter_artigo'),
    path('listar-artigos/', listar_artigos, name='listar_artigos'),

    path('deferir-artigo/<int:artigo_id>/', deferir_artigo, name='deferir_artigo'),
    path('indeferir-artigo/<int:artigo_id>/', indeferir_artigo, name='indeferir_artigo'),

    path('pagina_de_sucesso/', pagina_de_sucesso, name='pagina_de_sucesso'),

    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),

    path('meus-artigos/', meus_artigos, name='meus_artigos'),
     path('excluir-artigo/<int:artigo_id>/', excluir_artigo, name='excluir_artigo'),
]
