# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 18:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20160309_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]
