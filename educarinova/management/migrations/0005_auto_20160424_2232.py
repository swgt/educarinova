# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-24 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20160422_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matriculation',
            name='status',
            field=models.CharField(choices=[('success', 'Ativo'), ('danger', 'Desativado'), ('warning', 'Em Análise'), ('info', 'Em Curso'), ('closed', 'Concluido')], max_length=10, null=True, verbose_name='situação'),
        ),
    ]
