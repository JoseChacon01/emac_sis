# Generated by Django 4.2 on 2023-05-28 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_endereco_bairro_nac_endereco_cidade_nac_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cidade',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='estado',
            name='pais_regiao',
        ),
        migrations.DeleteModel(
            name='Bairro',
        ),
        migrations.DeleteModel(
            name='Cidade',
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
        migrations.DeleteModel(
            name='Pais_Regiao',
        ),
    ]
