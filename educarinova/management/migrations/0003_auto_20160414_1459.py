# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-14 14:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20160414_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commoninfo',
            old_name='cpf',
            new_name='CPF',
        ),
    ]
