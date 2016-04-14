# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-13 19:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import educarinova.management.models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_auto_20160412_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nome do custo')),
                ('value', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='valor')),
                ('monthly', models.BooleanField(default=False, verbose_name='mensal?')),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalCostAcquired',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.PositiveIntegerField(verbose_name='mês de cotratação')),
                ('additional_cost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.AdditionalCost', verbose_name='custo adicional')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreement', models.BooleanField(default=False, verbose_name='acordo?')),
                ('months_related', models.CharField(max_length=100, verbose_name='meses de referência')),
            ],
        ),
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StatusPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Aguardando', 'Aguardando'), ('Cancelado', 'Cancelado'), ('Pago', 'Pago')], max_length=15, verbose_name='status do pagamento')),
                ('date', models.DateField(verbose_name='data de atualização')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Payment', verbose_name='pagamento')),
            ],
        ),
        migrations.CreateModel(
            name='TuitionFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_tuition_fee', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='desconto na mensalidade')),
                ('reason_discount_tuition_fee', models.CharField(max_length=255, verbose_name='motivo do desconto')),
                ('expiration_day', models.PositiveIntegerField(verbose_name='dia de vencimento')),
                ('frequency_payment', models.CharField(choices=[('Mensal', 'Mensal'), ('Bimestral', 'Bimestral'), ('Trimestral', 'Trimestral'), ('Semestral', 'Semestral'), ('Anual', 'Anual')], max_length=30, verbose_name='frequencia de pagamento')),
            ],
        ),
        migrations.RemoveField(
            model_name='class',
            name='matriculation',
        ),
        migrations.RemoveField(
            model_name='matriculation',
            name='attendance',
        ),
        migrations.RemoveField(
            model_name='matriculation',
            name='score',
        ),
        migrations.RemoveField(
            model_name='student',
            name='matriculation',
        ),
        migrations.RemoveField(
            model_name='student',
            name='unit',
        ),
        migrations.AddField(
            model_name='class',
            name='period',
            field=models.CharField(choices=[('Meio Periodo', 'Meio Periodo'), ('Integral', 'Integral')], default='periodo', max_length=10, verbose_name='período'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class',
            name='shift',
            field=models.CharField(choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Noturno', 'Noturno'), ('Outro', 'Outro')], default='shift', max_length=10, verbose_name='turno'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class',
            name='value_tuition_fee',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=5, verbose_name='mensalidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matriculation',
            name='school_class',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.Class', verbose_name='turma'),
        ),
        migrations.AddField(
            model_name='matriculation',
            name='student',
            field=models.ForeignKey(null=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='management.Student', verbose_name='aluno'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='CEP',
            field=models.CharField(max_length=10, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='matriculation',
            name='number_matriculation',
            field=models.IntegerField(default=educarinova.management.models.random_string, verbose_name='matricula'),
        ),
        migrations.AlterField(
            model_name='matriculation',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Desativado', 'Desativado'), ('Em Análise', 'Em Análise'), ('Em Curso', 'Em Curso'), ('Concluido', 'Concluido')], max_length=10, null=True, verbose_name='situação'),
        ),
        migrations.AlterField(
            model_name='student',
            name='commoninfo_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='management.CommonInfo'),
        ),
        migrations.AddField(
            model_name='payment',
            name='matriculation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Matriculation', verbose_name='matricula'),
        ),
        migrations.AddField(
            model_name='additionalcostacquired',
            name='matriculation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Matriculation', verbose_name='matricula'),
        ),
        migrations.AddField(
            model_name='matriculation',
            name='report_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.ReportCard', verbose_name='boletim'),
        ),
        migrations.AddField(
            model_name='matriculation',
            name='tuition_fee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.TuitionFee', verbose_name='mensalidade'),
            preserve_default=False,
        ),
    ]
