# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-12 15:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import educarinova.management.models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20160412_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='matriculation',
            name='attendance',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='management.Attendance', verbose_name='frequência'),
        ),
        migrations.AddField(
            model_name='matriculation',
            name='score',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.Score', verbose_name='nota'),
        ),
        migrations.AddField(
            model_name='class',
            name='matriculation',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='management.Matriculation', verbose_name='matricula'),
        ),
    ]
