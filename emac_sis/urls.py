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
]
