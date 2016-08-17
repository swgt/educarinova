from random import randint

from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.utils import timezone

from django.utils.html import format_html


def random_string():
    number_random = randint(10000, 99999)
    current_date = date.today().year
    return str(current_date) + str(number_random)


class School(models.Model):
    company_name = models.CharField('nome da escola', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=14, primary_key=True)
    number_inep = models.CharField('inscrição do INEP', max_length=100)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'escolas'
        verbose_name = 'escola'
        ordering = ('-created_at',)

    def __str__(self):
        return self.company_name


class Address(models.Model):
    cep = models.CharField('CEP', max_length=10)
    TYPES_OF_STREETS = (
        ('Rua', 'Rua'),
        ('Avenida', 'Avenida')
    )
    type_of_street = models.CharField('tipo de logradouro', max_length=100, choices=TYPES_OF_STREETS)
    street = models.CharField('logradouro', max_length=100)
    house_number = models.CharField('número', max_length=6)
    complement = models.CharField('complemento', max_length=100, null=True, blank=True)
    district = models.CharField('bairro', max_length=100)
    city = models.CharField('cidade', max_length=100)
    state = models.CharField('estado', max_length=100)

    def __str__(self):
        return self.cep


class Contact(models.Model):
    cell_phone = models.CharField('celular', max_length=20)
    cell_phone_secondary = models.CharField('outro celular', max_length=20, null=True, blank=True)
    phone = models.CharField('telefone¹', max_length=20, null=True, blank=True)
    phone_secondary = models.CharField('telefone²', max_length=20, null=True, blank=True)
    email = models.EmailField('e-mail')
    fax = models.CharField('fax', max_length=20, null=True, blank=True)

    def __str__(self):
        return self.email


class Unit(models.Model):
    name = models.CharField('nome da unidade', max_length=100)
    school = models.ForeignKey(School, verbose_name="escola")
    contact = models.ForeignKey(Contact, verbose_name="contato")
    address = models.ForeignKey(Address, verbose_name="endereço", default=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    def __str__(self):
        return str(self.school) + " - " + self.name


class Classroom(models.Model):
    identification = models.CharField('Identificação da sala', max_length=100)
    TYPES_CLASSROOM = (
        ('Sala de Aula', 'Sala de Aula'),
        ('Laboratório', 'Laboratório'),
        ('Outro', 'Outro'),
    )
    type = models.CharField('tipo de sala', max_length=30, choices=TYPES_CLASSROOM)
    unit = models.ForeignKey(Unit, verbose_name='unidade escolar')


class CommonInfo(models.Model):
    name = models.CharField('nome', max_length=150)
    cpf = models.CharField('CPF', max_length=14, primary_key=True)
    date_of_birth = models.DateField('data de nascimento')
    RACES = (
        ('Branco(a)', 'Branco(a)'),
        ('Pardo(a)', 'Pardo(a)'),
        ('Preto(a)', 'Preto(a)'),
        ('Amarelo(a)', 'Amarelo(a)'),
        ('Indígeno(a)', 'Indígeno(a)'),
    )
    race = models.CharField('raça', max_length=12, choices=RACES)
    rg = models.CharField('RG', max_length=100)
    DISPATCH_ENTITIES_RG = (
        ('SSP', 'SSP'),
        ('IML', 'IML'),
        ('ITEP', 'ITEP'),
        ('ITCP', 'ITCP'),
    )
    dispatch_entity_rg = models.CharField('orgão expedidor do RG', max_length=4, choices=DISPATCH_ENTITIES_RG)
    GENDERS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    gender = models.CharField('sexo', max_length=1, choices=GENDERS)
    NATIONALITIES = (
        ('AR', 'Argentino(a)'),
        ('BR', 'Brasileiro(a)'),
        ('CA', 'Canadiano(a)'),
        ('CL', 'Chileno(a)'),
        ('CO', 'Colombiano(a)'),
        ('CU', 'Cubano(a)'),
        ('US', 'Norte-americano(a)'),
        ('MX', 'Mexicano(a)'),
        ('VE', 'Venezuelano(a)'),
    )
    nationality = models.CharField('nacionalidade', max_length=2, choices=NATIONALITIES)
    naturalness = models.CharField('naturalidade', max_length=100)


class Attendance(models.Model):
    pass


class Score(models.Model):
    pass


class ReportCard(models.Model):
    pass


class Student(CommonInfo):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='usuario', null=True, blank=True)
    contact = models.ForeignKey(Contact, verbose_name="contato", null=True, blank=True)
    address = models.ForeignKey(Address, verbose_name="endereço", null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='created_by_user', verbose_name='criado por', null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='updated_by_user', verbose_name='atualizado por', null=True, blank=True)
    STATUS = (
        ('info', 'Ativo'),
        ('danger', 'Desativado'),
    )
    status = models.CharField('situação', max_length=10, choices=STATUS, null=True, default='info')

    class Meta:
        verbose_name_plural = 'alunos'
        verbose_name = 'aluno'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_verify_if_matriculate(self):
        enrollment_students = self.matriculation_set.all()

        if not enrollment_students:
            return format_html('<span class="status status-{}">{}</span>',
                               'neutral', 'Não Matriculado')

        for index in range(len(enrollment_students)):
            enrollment_student = enrollment_students[len(enrollment_students)-1]
            return format_html('<span class="status status-{}">{}</span>',
                               enrollment_student.status,
                               enrollment_student.get_status_display())


class Employee(CommonInfo):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matriculation = models.CharField('matrícula', max_length=100, primary_key=True)
    unit = models.ForeignKey(Unit, verbose_name="unidade", default=False)
    contact = models.ForeignKey(Contact, verbose_name="contato", default=False)
    address = models.ForeignKey(Address, verbose_name="endereço", default=False)
    FUNCTIONS = (
        ('Diretor(a)', 'Diretor(a)'),
        ('Vice-Diretor(a)', 'Vice-Diretor(a)'),
        ('Secretário(a)', 'Secretário(a)'),
        ('Coordenador(a)', 'Coordenador(a)'),
        ('Pedagogo(a)', 'Pedagogo(a)'),
        ('Professor(a)', 'Professor(a)'),
        ('Porteiro(a)', 'Porteiro(a)'),
        ('Outro', 'Outro'),
    )
    function = models.CharField('função', max_length=25, choices=FUNCTIONS)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    def __str__(self):
        return self.name


class Serie(models.Model):
    serie = models.CharField('série', max_length=20)
    LEVELS = (
        ('Creche', 'Creche'),
        ('Infantil', 'Infantil'),
        ('Fundamental', 'Fundamental'),
        ('Médio', 'Médio'),
        ('Outro', 'Outro'),
    )
    level = models.CharField('nível', max_length=25, choices=LEVELS)

    def __str__(self):
        return self.serie + ". Ensino " + self.level


class Class(models.Model):
    name = models.CharField('nome da turma', max_length=30)
    serie = models.ForeignKey(Serie, verbose_name="serie", null=True)
    academic_year = models.IntegerField('ano letivo', default=date.today().year)
    unit = models.ForeignKey(Unit, verbose_name='unidade escolar', null=True)
    SHIFTS = (
        ('M','Matutino'),
        ('V','Vespertino'),
        ('N','Noturno'),
        ('O','Outro'),
        )
    shift = models.CharField('turno de aula', max_length=10, choices=SHIFTS)
    PERIODS = (
        ('Meio Periodo','Meio Periodo'),
        ('Integral','Integral'),
        )
    period = models.CharField('período', max_length=12, choices=PERIODS)

    def __str__(self):
        return str(self.serie) + ", " + self.get_shift_display() + " / " +self.name

class SystemClass(models.Model):
    SYSTEMS_CHOICES = (
        ('Somente Aula','Somente Aula'),
        ('Meio Período','Meio Período'),
        ('Integral','Integral')
    )
    system = models.CharField('tipo de sistema', max_length=15, choices=SYSTEMS_CHOICES)
    start_time = models.TimeField('hora de início')
    end_time = models.TimeField('hora de fim')
    vacancies = models.CharField('vagas disponíveis', max_length=10, default=0)

class ClassSystemClass(models.Model):
    classv = models.ForeignKey(Class, verbose_name='turma')
    system_class = models.ForeignKey(SystemClass, verbose_name='sistema possível na turma')
    value_tuition_fee = models.DecimalField('mensalidade (R$)', max_digits=5, decimal_places=2, default=0.00)


class TuitionFee(models.Model):
    discount_tuition_fee = models.DecimalField('desconto na mensalidade', max_digits=3, decimal_places=0, null=True, blank=True, default=0)
    reason_discount_tuition_fee = models.CharField('motivo do desconto', max_length=255, null=True, blank=True)
    EXPIRATION_DAYS = (
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('20', '20'),
        ('25', '25')
        )
    expiration_day = models.CharField('dia de vencimento', max_length=2, choices=EXPIRATION_DAYS, default=5)
    FREQUENCY_PAYMENTS = (
        ('Mensal', 'Mensal'),
        ('Bimestral', 'Bimestral'),
        ('Trimestral', 'Trimestral'),
        ('Semestral', 'Semestral'),
        ('Anual', 'Anual'),
        )
    frequency_payment = models.CharField('frequência de pagamento', max_length=30, choices=FREQUENCY_PAYMENTS, default="Mensal")

    def __str__(self):
        return self.frequency_payment


class Matriculation(models.Model):
    number_matriculation = models.IntegerField('matrícula', default=random_string)
    school_class = models.ForeignKey(ClassSystemClass, verbose_name="turma", null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE,  verbose_name='aluno', null=True, blank=True)
    STATUS = (
        ('info', 'Cursando'),
        ('warning', 'Em Análise'),
        ('success', 'Concluido'),
        ('danger', 'Cancelado'),
    )
    status = models.CharField('situação', max_length=10, choices=STATUS, null=True, default='Em Curso')
    report_card = models.ForeignKey(ReportCard, verbose_name="boletim", null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True, null=True)
    tuition_fee = models.ForeignKey(TuitionFee, verbose_name='mensalidade', null=True, blank=True)

    def __str__(self):
        return str(self.number_matriculation)

    def get_colored_status(self):
        return format_html('<span class="status status-{}">{}</span>',
                           self.status,
                           self.get_status_display())


class Subject(models.Model):
    name = models.CharField('nome da disciplina', max_length=50)


class AdditionalCost(models.Model):
    name = models.CharField('nome do custo', max_length=50)
    value = models.DecimalField('valor', max_digits=5, decimal_places=2)
    monthly = models.BooleanField('mensal?', default=False)


class AdditionalCostAcquired(models.Model):
    matriculation = models.ForeignKey(Matriculation, verbose_name='matricula')
    additional_cost = models.ForeignKey(AdditionalCost, verbose_name='custo adicional')
    MONTHS = (
        (1, 'Janeiro'),
        (2, 'Fevereiro'),
        (3, 'Março'),
        (4, 'Abril'),
        (5, 'Maio'),
        (6, 'Junho'),
        (7, 'Julho'),
        (8, 'Agosto'),
        (9, 'Setembro'),
        (10, 'Outubro'),
        (11, 'Novembro'),
        (12, 'Dezembro'),
        )
    month = models.PositiveIntegerField('mês de cotratação', choices=MONTHS)


class Payment(models.Model):
    matriculation = models.ForeignKey(Matriculation, verbose_name='matricula')
    agreement = models.BooleanField('acordo?', default=False)
    months_related = models.CharField('meses de referência', max_length=100)


class StatusPayment(models.Model):
    payment = models.ForeignKey(Payment, verbose_name='pagamento')
    STATUS_PAYMENT = (
        ('Aguardando', 'Aguardando'),
        ('Cancelado', 'Cancelado'),
        ('Pago', 'Pago')
        )
    status = models.CharField('status do pagamento', max_length=15, choices=STATUS_PAYMENT)
    date = models.DateField('data de atualização')


class Carrier(models.Model):
    BANK_CODS = (
        ('001', '001 - Banco do Brasil'),
        ('003', '003 - Banco da Amazônia'),
        ('004', '004 - Banco do Nordeste'),
        ('033', '033 - Banco Santander'),
        ('104', '104 - Caixa Econômica'),
        ('237', '237 - Banco Bradesco'),
        ('241', '241 - Banco Itaú'),
        ('256', '256 - Banco Real'),
        ('239', '239 - Banco HSBC'),
        ('748', '748 - SISCRED'),
        ('756', '756 - Bancoob/Sicoob'),
        ('999', '999 - Cobrança Sistema Local')
    )
    bank_cod = models.CharField('código do banco', max_length=15, choices=BANK_CODS)
    description = models.CharField('descrição', max_length=100)
    agency = models.CharField('agência', max_length=10)
    agency_dv = models.CharField('dígito verificar da agência', max_length=1)
    transferor_account = models.CharField('conta do cedente', max_length=10)
    transferor_account_dv = models.CharField('dígito verificador da conta do cedente', max_length=1)
    agreement = models.CharField('covênio', max_length=10)
    agreement_automatic_debit = models.CharField('covênio débito automático', max_length=20)
    contract = models.CharField('contrato', max_length=10)
    wallet = models.CharField('carteira', max_length=10)
    transferor_name = models.CharField('nome do cedente', max_length=50)
    cpf_cnpj_transferor = models.CharField('CPF/CNPJ do cedente', max_length=50)
    default_carrier = models.BooleanField('potador padrão?', default=False)
    our_number = models.CharField('nosso número', max_length=10)
    TYPES_BANK_SLIP = (
        ('1', 'Título c/ Registro - Envio pelo Cedente'),
        ('11', 'Título c/ Registro - Envio pelo Banco'),
        ('2', '004 - Título s/ Registro - Envio pelo Cedente'),
        ('22', 'Título s/ Registro - Envio pelo Banco')
    )
    type_bank_slip = models.CharField('tipo de título', max_length=50, choices=TYPES_BANK_SLIP, default="2")
    check_days_shipment =  models.IntegerField('dias de antencedência para gerar a remessa', default=0)
    STATUS = (
        ('success', 'Ativo'),
        ('danger', 'Desativado')
    )
    status = models.CharField('situação', max_length=10, choices=STATUS, default="success")


class TemplateBankSlip(models.Model):
    payment_local = models.CharField('local de pagamento', max_length=100)
    instruction1 = models.CharField('instrução 1', max_length=100)
    instruction2 = models.CharField('instrução 2', max_length=100)
    instruction3 = models.CharField('instrução 3', max_length=100)
    instruction4 = models.CharField('instrução 4', max_length=100)
    instruction5 = models.CharField('instrução 5', max_length=100)
    rate_bank_slip = models.DecimalField('taxa do boleto (R$)', max_digits=5, decimal_places=2, default=0.00)
    include_rate = models.BooleanField('incluir taxa do boleto no valor?', default=False)
    penalty = models.IntegerField('multa por atraso (%)')
    interest = models.IntegerField('juros por atraso (%)')
    discount_due_date = models.DecimalField('desconto até o vencimento', max_digits=5, decimal_places=2, default=0.00)
    default_template = models.BooleanField('template padrão?', default=False)


class Responsible(CommonInfo):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='usuario', null=True, blank=True)
    contact = models.ForeignKey(Contact, verbose_name="contato", null=True, blank=True)
    address = models.ForeignKey(Address, verbose_name="endereço", null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)


class ResponsibleStudent(models.Model):
    student = models.ForeignKey(Student, verbose_name="estudante")
    responsible = models.ForeignKey(Responsible, verbose_name="responsável")
    KINSHIPS = (
        ('Pai/Mãe', 'Pai/Mãe'),
        ('Irmão/Irmã', 'Irmão/Irmã'),
        ('Tio(a)', 'Tio(a)'),
        ('Avô(ó)', 'Avô(ó)'),
        ('Outro parentesco', 'Outro parentesco')
    )
    kinship = models.CharField('parentesco', max_length=20, choices=KINSHIPS)


class CostCenter(models.Model):
    pass


class BankSlip(models.Model):
    payment = models.ForeignKey(Payment, verbose_name="pagamento de referência")
    #estudar.. no sgp ele relaciona com o codigo do contrato
    matriculation = models.ForeignKey(Matriculation, verbose_name="matricula de referência")
    template_bank_slip = models.ForeignKey(TemplateBankSlip, verbose_name="template do boleto")
    carrier = models.ForeignKey(Carrier, verbose_name="portador")
    #podemos implementar aqui um default value, que puxa do banco o ultimo
    #numero gerado e incremena 1
    document_number = models.IntegerField('número do documento')
    digitable_line = models.CharField('linha digitável', max_length=60)
    cost_center = models.ForeignKey(CostCenter, verbose_name="centro de custo")
    our_number = models.CharField('nosso número', max_length=25)
    demonstrative = models.CharField('demostrativo', max_length=100)
    bank_slip_value = models.DecimalField('valor do boleto', max_digits=5, decimal_places=2, default=0.00)
    emission_date = models.DateTimeField('data de emissão', auto_now_add=True)
    MODES_GERATION = (
        ('lote', 'Lote'),
        ('avulso', 'Avulso')
    )
    mode_geration = models.CharField('situação', max_length=10, choices=MODES_GERATION)
    due_date = models.DateTimeField('data de vencimento', auto_now_add=True)


class ReceiveLocation(models.Model):
    pass


class StatusBankSlip(models.Model):
    bank_slip = models.ForeignKey(BankSlip, verbose_name="boleto de referência")
    STATUS = (
        ('gerado', 'Gerado'),
        ('pago', 'Pago'),
        ('cancelado', 'Cancelado')
    )
    status = models.CharField('situação', max_length=10, choices=STATUS, default="gerado")
    create_at = models.DateTimeField('criado em', auto_now_add=True)


    #onde guardaremos os dados de pagamento de um boleto?
    #como valor pago, desconto, 
class PaymentBankSlip(models.Model):
    bank_slip = models.ForeignKey(BankSlip, verbose_name="boleto de referência")
    receive_location = models.ForeignKey(ReceiveLocation, verbose_name="ponto de recebimento")
    cost_center = models.ForeignKey(CostCenter, verbose_name="centro de custo")
    PAYMENT_METHODS = (
        ('Dinheiro','Dinheiro'),
        ('Transferência Bancária','Transferência Bancária'),
        ('Cartão de Crédito','Cartão de Crédito'),
        ('Cartão de Débito','Cartão de Débito'),
        ('Cheque à Vista','Cheque à Vista'),
        ('Cheque à Prazo','Cheque à Prazo'),
    ) 
    payment_method = models.CharField('método de pagamento', max_length=25, choices=PAYMENT_METHODS)
    #de acordo com o valor pago, e disconto. é calculado o acréscimo/desconto para o mês seguinte
    amount_paid = models.DecimalField('valor pago', max_digits=5, decimal_places=2, default=0.00)
    discount = models.DecimalField('valor pago', max_digits=5, decimal_places=2, default=0.00)
    reason_discount = models.CharField('motivo do desconto', max_length=100)
    note = models.CharField('observação', max_length=100)
    date_payment = models.DateTimeField('data de pagamento') 
    date_process = models.DateTimeField('data de processamento', auto_now_add=True) 

class AccretionDiscount(models.Model):
    #estudar.. no sgp ele relaciona com o codigo do contrato
    matriculation = models.ForeignKey(Matriculation, verbose_name="matricula de referência")
    value = models.DecimalField('valor do acréscimo ou desconto', max_digits=5, decimal_places=2, default=0.00)
    justification = models.CharField('justificativa', max_length=100)
    total_plots = models.IntegerField('total de parcelas')
    note = models.CharField('observação', max_length=100)
    TYPES = (
        ('Fixo','Fixo'),
        ('Temporário','Temporário'),
        )
    #Fixo: Acrescimo/Desconto sempre será aplicado. 
    #Temporário: Acrescimo/Desconto será aplicado pela quantidade de parcelas. 
    type_accretion_discount = models.CharField('situação', max_length=10, choices=TYPES)
    MODES_GERATION = (
        ('lote', 'Lote'),
        ('avulso', 'Avulso')
    )
    mode_geration = models.CharField('situação', max_length=10, choices=MODES_GERATION)


class CashRegister(models.Model):
    OPERATIONS = (
        ('Entrada', 'Entrada'),
        ('Saída', 'Saída')
    )
    operation = models.CharField('operação', max_length=10, choices=OPERATIONS)
    receive_location = models.ForeignKey(ReceiveLocation, verbose_name="ponto de recebimento")
    cost_center = models.ForeignKey(CostCenter, verbose_name="centro de custo")
    PAYMENT_METHODS = (
        ('Dinheiro','Dinheiro'),
        ('Transferência Bancária','Transferência Bancária'),
        ('Cartão de Crédito','Cartão de Crédito'),
        ('Cartão de Débito','Cartão de Débito'),
        ('Cheque à Vista','Cheque à Vista'),
        ('Cheque à Prazo','Cheque à Prazo'),
    ) 
    payment_method = models.CharField('método de pagamento', max_length=25, choices=PAYMENT_METHODS)
    value = models.DecimalField('valor', max_digits=5, decimal_places=2, default=0.00)
    description = models.CharField('observação', max_length=100)
    accrual_date = models.DateTimeField('data de competência', auto_now_add=True) 