# Generated by Django 4.2 on 2023-05-11 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_usuario_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='bairro',
        ),
    ]
