# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-09 15:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0006_auto_20160425_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccretionDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='valor do acréscimo ou desconto')),
                ('justification', models.CharField(max_length=100, verbose_name='justificativa')),
                ('total_plots', models.IntegerField(verbose_name='total de parcelas')),
                ('note', models.CharField(max_length=100, verbose_name='observação')),
                ('type_accretion_discount', models.CharField(choices=[('Fixo', 'Fixo'), ('Temporário', 'Temporário')], max_length=10, verbose_name='situação')),
                ('mode_geration', models.CharField(choices=[('lote', 'Lote'), ('avulso', 'Avulso')], max_length=10, verbose_name='situação')),
            ],
        ),
        migrations.CreateModel(
            name='BankSlip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_number', models.IntegerField(verbose_name='número do documento')),
                ('digitable_line', models.CharField(max_length=60, verbose_name='linha digitável')),
                ('our_number', models.CharField(max_length=25, verbose_name='nosso número')),
                ('demonstrative', models.CharField(max_length=100, verbose_name='demostrativo')),
                ('bank_slip_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='valor do boleto')),
                ('emission_date', models.DateTimeField(auto_now_add=True, verbose_name='data de emissão')),
                ('mode_geration', models.CharField(choices=[('lote', 'Lote'), ('avulso', 'Avulso')], max_length=10, verbose_name='situação')),
                ('due_date', models.DateTimeField(auto_now_add=True, verbose_name='data de vencimento')),
            ],
        ),
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_cod', models.CharField(choices=[('001', '001 - Banco do Brasil'), ('003', '003 - Banco da Amazônia'), ('004', '004 - Banco do Nordeste'), ('033', '033 - Banco Santander'), ('104', '104 - Caixa Econômica'), ('237', '237 - Banco Bradesco'), ('241', '241 - Banco Itaú'), ('256', '256 - Banco Real'), ('239', '239 - Banco HSBC'), ('748', '748 - SISCRED'), ('756', '756 - Bancoob/Sicoob'), ('999', '999 - Cobrança Sistema Local')], max_length=15, verbose_name='código do banco')),
                ('description', models.CharField(max_length=100, verbose_name='descrição')),
                ('agency', models.CharField(max_length=10, verbose_name='agência')),
                ('agency_dv', models.CharField(max_length=1, verbose_name='dígito verificar da agência')),
                ('transferor_account', models.CharField(max_length=10, verbose_name='conta do cedente')),
                ('transferor_account_dv', models.CharField(max_length=1, verbose_name='dígito verificador da conta do cedente')),
                ('agreement', models.CharField(max_length=10, verbose_name='covênio')),
                ('agreement_automatic_debit', models.CharField(max_length=20, verbose_name='covênio débito automático')),
                ('contract', models.CharField(max_length=10, verbose_name='contrato')),
                ('wallet', models.CharField(max_length=10, verbose_name='carteira')),
                ('transferor_name', models.CharField(max_length=50, verbose_name='nome do cedente')),
                ('cpf_cnpj_transferor', models.CharField(max_length=50, verbose_name='CPF/CNPJ do cedente')),
                ('default_carrier', models.BooleanField(default=False, verbose_name='potador padrão?')),
                ('our_number', models.CharField(max_length=10, verbose_name='nosso número')),
                ('type_bank_slip', models.CharField(choices=[('1', 'Título c/ Registro - Envio pelo Cedente'), ('11', 'Título c/ Registro - Envio pelo Banco'), ('2', '004 - Título s/ Registro - Envio pelo Cedente'), ('22', 'Título s/ Registro - Envio pelo Banco')], default='2', max_length=50, verbose_name='tipo de título')),
                ('check_days_shipment', models.IntegerField(default=0, verbose_name='dias de antencedência para gerar a remessa')),
                ('status', models.CharField(choices=[('success', 'Ativo'), ('danger', 'Desativado')], default='success', max_length=10, verbose_name='situação')),
            ],
        ),
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Responsible',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='management.CommonInfo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.Address', verbose_name='endereço')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.Contact', verbose_name='contato')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            bases=('management.commoninfo',),
        ),
        migrations.CreateModel(
            name='ResponsibleStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kinship', models.CharField(choices=[('Pai/Mãe', 'Pai/Mãe'), ('Irmão/Irmã', 'Irmão/Irmã'), ('Tio(a)', 'Tio(a)'), ('Avô(ó)', 'Avô(ó)'), ('Outro parentesco', 'Outro parentesco')], max_length=20, verbose_name='situação')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Responsible', verbose_name='responsável')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Student', verbose_name='estudante')),
            ],
        ),
        migrations.CreateModel(
            name='StatusBankSlip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('gerado', 'Gerado'), ('pago', 'Pago'), ('cancelado', 'Cancelado')], default='gerado', max_length=10, verbose_name='situação')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('bank_slip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.BankSlip', verbose_name='boleto de referência')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateBankSlip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_local', models.CharField(max_length=100, verbose_name='local de pagamento')),
                ('instruction1', models.CharField(max_length=100, verbose_name='instrução 1')),
                ('instruction2', models.CharField(max_length=100, verbose_name='instrução 2')),
                ('instruction3', models.CharField(max_length=100, verbose_name='instrução 3')),
                ('instruction4', models.CharField(max_length=100, verbose_name='instrução 4')),
                ('instruction5', models.CharField(max_length=100, verbose_name='instrução 5')),
                ('rate_bank_slip', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='taxa do boleto (R$)')),
                ('include_rate', models.BooleanField(default=False, verbose_name='incluir taxa do boleto no valor?')),
                ('penalty', models.IntegerField(verbose_name='multa por atraso (%)')),
                ('interest', models.IntegerField(verbose_name='juros por atraso (%)')),
                ('discount_due_date', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='desconto até o vencimento')),
                ('default_template', models.BooleanField(default=False, verbose_name='template padrão?')),
            ],
        ),
        migrations.AlterField(
            model_name='matriculation',
            name='status',
            field=models.CharField(choices=[('info', 'Cursando'), ('warning', 'Em Análise'), ('success', 'Concluido'), ('danger', 'Cancelado')], default='Em Curso', max_length=10, null=True, verbose_name='situação'),
        ),
        migrations.AddField(
            model_name='bankslip',
            name='carrier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Carrier', verbose_name='portador'),
        ),
        migrations.AddField(
            model_name='bankslip',
            name='cost_center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.CostCenter', verbose_name='centro de custo'),
        ),
        migrations.AddField(
            model_name='bankslip',
            name='matriculation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Matriculation', verbose_name='matricula de referência'),
        ),
        migrations.AddField(
            model_name='bankslip',
            name='template_bank_slip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.TemplateBankSlip', verbose_name='template do boleto'),
        ),
        migrations.AddField(
            model_name='accretiondiscount',
            name='matriculation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Matriculation', verbose_name='matricula de referência'),
        ),
    ]
