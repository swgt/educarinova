# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-06 17:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20160406_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='ano_letivo',
            new_name='academic_year',
        ),
        migrations.RenameField(
            model_name='class',
            old_name='vagas',
            new_name='vacancies',
        ),
    ]