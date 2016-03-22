# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-22 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_auto_20160313_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='cell_phone_secondary',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='outro celular'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='fax',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='fax'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='telefone¹'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_secondary',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='telefone²'),
        ),
    ]