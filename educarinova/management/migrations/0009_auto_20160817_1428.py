# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-17 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_auto_20160628_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemclass',
            name='vacancies',
        ),
        migrations.AddField(
            model_name='classsystemclass',
            name='vacancies',
            field=models.CharField(default=0, max_length=10, verbose_name='vagas disponíveis'),
        ),
        migrations.AlterField(
            model_name='systemclass',
            name='system',
            field=models.CharField(max_length=15, verbose_name='tipo de sistema'),
        ),
    ]