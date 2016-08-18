# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-17 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_auto_20160524_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(choices=[('Entrada', 'Entrada'), ('Saída', 'Saída')], max_length=10, verbose_name='operação')),
                ('payment_method', models.CharField(choices=[('Dinheiro', 'Dinheiro'), ('Transferência Bancária', 'Transferência Bancária'), ('Cartão de Crédito', 'Cartão de Crédito'), ('Cartão de Débito', 'Cartão de Débito'), ('Cheque à Vista', 'Cheque à Vista'), ('Cheque à Prazo', 'Cheque à Prazo')], max_length=25, verbose_name='método de pagamento')),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='valor')),
                ('description', models.CharField(max_length=100, verbose_name='observação')),
                ('accrual_date', models.DateTimeField(auto_now_add=True, verbose_name='data de competência')),
                ('cost_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.CostCenter', verbose_name='centro de custo')),
            ],
        ),
        migrations.CreateModel(
            name='ClassSystemClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_tuition_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='mensalidade (R$)')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentBankSlip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('Dinheiro', 'Dinheiro'), ('Transferência Bancária', 'Transferência Bancária'), ('Cartão de Crédito', 'Cartão de Crédito'), ('Cartão de Débito', 'Cartão de Débito'), ('Cheque à Vista', 'Cheque à Vista'), ('Cheque à Prazo', 'Cheque à Prazo')], max_length=25, verbose_name='método de pagamento')),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='valor pago')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='valor pago')),
                ('reason_discount', models.CharField(max_length=100, verbose_name='motivo do desconto')),
                ('note', models.CharField(max_length=100, verbose_name='observação')),
                ('date_payment', models.DateTimeField(verbose_name='data de pagamento')),
                ('date_process', models.DateTimeField(auto_now_add=True, verbose_name='data de processamento')),
            ],
        ),
        migrations.CreateModel(
            name='ReceiveLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SystemClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(choices=[('Somente Aula', 'Somente Aula'), ('Meio Período', 'Meio Período'), ('Integral', 'Integral')], max_length=15, verbose_name='tipo de sistema')),
                ('start_time', models.TimeField(verbose_name='hora de início')),
                ('end_time', models.TimeField(verbose_name='hora de fim')),
                ('vacancies', models.CharField(default=0, max_length=10, verbose_name='vagas disponíveis')),
            ],
        ),
        migrations.RemoveField(
            model_name='class',
            name='vacancies',
        ),
        migrations.RemoveField(
            model_name='class',
            name='value_tuition_fee',
        ),
        migrations.AddField(
            model_name='bankslip',
            name='payment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='management.Payment', verbose_name='pagamento de referência'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='class',
            name='shift',
            field=models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno'), ('O', 'Outro')], max_length=10, verbose_name='turno de aula'),
        ),
        migrations.AlterField(
            model_name='matriculation',
            name='school_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.ClassSystemClass', verbose_name='turma'),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('info', 'Ativo'), ('danger', 'Desativado')], default='info', max_length=10, null=True, verbose_name='situação'),
        ),
        migrations.AlterField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='atualizado em'),
        ),
        migrations.AlterField(
            model_name='tuitionfee',
            name='expiration_day',
            field=models.CharField(choices=[('5', '5'), ('10', '10'), ('15', '15'), ('20', '20'), ('25', '25')], default=5, max_length=2, verbose_name='dia de vencimento'),
        ),
        migrations.AddField(
            model_name='paymentbankslip',
            name='bank_slip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.BankSlip', verbose_name='boleto de referência'),
        ),
        migrations.AddField(
            model_name='paymentbankslip',
            name='cost_center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.CostCenter', verbose_name='centro de custo'),
        ),
        migrations.AddField(
            model_name='paymentbankslip',
            name='receive_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.ReceiveLocation', verbose_name='ponto de recebimento'),
        ),
        migrations.AddField(
            model_name='classsystemclass',
            name='classv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Class', verbose_name='turma'),
        ),
        migrations.AddField(
            model_name='classsystemclass',
            name='system_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.SystemClass', verbose_name='sistema possível na turma'),
        ),
        migrations.AddField(
            model_name='cashregister',
            name='receive_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.ReceiveLocation', verbose_name='ponto de recebimento'),
        ),
    ]
