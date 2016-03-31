# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-31 01:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CEP', models.CharField(max_length=9, verbose_name='CEP')),
                ('type_of_street', models.CharField(max_length=100, verbose_name='tipo de logradouro')),
                ('street', models.CharField(max_length=100, verbose_name='logradouro')),
                ('house_number', models.CharField(max_length=6, verbose_name='número')),
                ('complement', models.CharField(blank=True, max_length=100, null=True, verbose_name='complemento')),
                ('district', models.CharField(max_length=100, verbose_name='bairro')),
                ('city', models.CharField(max_length=100, verbose_name='cidade')),
                ('state', models.CharField(max_length=100, verbose_name='estado')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='nome da turma')),
                ('ano_letivo', models.IntegerField(default=2016, verbose_name='ano letivo')),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=100, verbose_name='Identificação da sala')),
                ('type', models.CharField(choices=[('Sala de Aula', 'Sala de Aula'), ('Laboratório', 'Laboratório'), ('Outro', 'Outro')], max_length=30, verbose_name='tipo de sala')),
            ],
        ),
        migrations.CreateModel(
            name='CommonInfo',
            fields=[
                ('name', models.CharField(max_length=150, verbose_name='nome')),
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='CPF')),
                ('date_of_birth', models.DateField(verbose_name='data de nascimento')),
                ('race', models.CharField(choices=[('Branco(a)', 'Branco(a)'), ('Pardo(a)', 'Pardo(a)'), ('Preto(a)', 'Preto(a)'), ('Amarelo(a)', 'Amarelo(a)'), ('Indígeno(a)', 'Indígeno(a)')], max_length=12, verbose_name='raça')),
                ('rg', models.CharField(max_length=100, verbose_name='RG')),
                ('dispatch_entity_rg', models.CharField(choices=[('SSP', 'SSP'), ('IML', 'IML'), ('ITEP', 'ITEP'), ('ITCP', 'ITCP')], max_length=4, verbose_name='orgão expedidor do RG')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='sexo')),
                ('nationality', models.CharField(choices=[('AR', 'Argentino(a)'), ('BR', 'Brasileiro(a)'), ('CA', 'Canadiano(a)'), ('CL', 'Chileno(a)'), ('CO', 'Colombiano(a)'), ('CU', 'Cubano(a)'), ('US', 'Norte-americano(a)'), ('MX', 'Mexicano(a)'), ('VE', 'Venezuelano(a)')], max_length=2, verbose_name='nacionalidade')),
                ('naturalness', models.CharField(max_length=100, verbose_name='naturalidade')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell_phone', models.CharField(max_length=20, verbose_name='celular')),
                ('cell_phone_secondary', models.CharField(blank=True, max_length=20, null=True, verbose_name='outro celular')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='telefone¹')),
                ('phone_secondary', models.CharField(blank=True, max_length=20, null=True, verbose_name='telefone²')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('fax', models.CharField(blank=True, max_length=20, null=True, verbose_name='fax')),
            ],
        ),
        migrations.CreateModel(
            name='Matriculation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('company_name', models.CharField(max_length=100, verbose_name='nome da escola')),
                ('cnpj', models.CharField(max_length=14, primary_key=True, serialize=False, verbose_name='CNPJ')),
                ('number_inep', models.CharField(max_length=100, verbose_name='inscrição do INEP')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
            ],
            options={
                'verbose_name': 'escola',
                'verbose_name_plural': 'escolas',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(max_length=20, verbose_name='série')),
                ('level', models.CharField(choices=[('Creche', 'Creche'), ('Infantil', 'Infantil'), ('Fundamental', 'Fundamental'), ('Médio', 'Médio'), ('Outro', 'Outro')], max_length=25, verbose_name='nível')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nome da disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome da unidade')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('address', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='management.Address', verbose_name='endereço')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Contact', verbose_name='contato')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.School', verbose_name='escola')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='management.CommonInfo')),
                ('matriculation', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='matrícula')),
                ('function', models.CharField(choices=[('Diretor(a)', 'Diretor(a)'), ('Vice-Diretor(a)', 'Vice-Diretor(a)'), ('Secretário(a)', 'Secretário(a)'), ('Coordenador(a)', 'Coordenador(a)'), ('Pedagogo(a)', 'Pedagogo(a)'), ('Professor(a)', 'Professor(a)'), ('Porteiro(a)', 'Porteiro(a)'), ('Outro', 'Outro')], max_length=25, verbose_name='função')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('address', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='management.Address', verbose_name='endereço')),
                ('contact', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='management.Contact', verbose_name='contato')),
                ('unit', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='management.Unit', verbose_name='unidade')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('management.commoninfo',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='management.CommonInfo')),
                ('matriculation', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='matrícula')),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Desativado', 'Desativado'), ('Em Curso', 'Em Curso'), ('Concluido', 'Concluido')], max_length=10, verbose_name='situação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('address', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='management.Address', verbose_name='endereço')),
                ('contact', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='management.Contact', verbose_name='contato')),
                ('unit', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='management.Unit', verbose_name='unidade')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'aluno',
                'verbose_name_plural': 'alunos',
                'ordering': ('-created_at',),
            },
            bases=('management.commoninfo',),
        ),
        migrations.AddField(
            model_name='classroom',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Unit', verbose_name='unidade escolar'),
        ),
        migrations.AddField(
            model_name='class',
            name='serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Serie', verbose_name='serie'),
        ),
        migrations.AddField(
            model_name='class',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Unit', verbose_name='unidade escolar'),
        ),
    ]
