# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-12 16:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20160412_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='matriculation',
            new_name='matricula',
        ),
    ]
