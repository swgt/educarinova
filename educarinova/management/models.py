from random import randint

from django.db import models
from django.contrib.auth.models import User
from datetime import date


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
    CEP = models.CharField('CEP', max_length=10)
    TYPE_OF_STREET_CHOICES = (
        ('Rua', 'Rua'),
        ('Avenida', 'Avenida')
    )
    type_of_street = models.CharField('tipo de logradouro', max_length=100, choices=TYPE_OF_STREET_CHOICES)
    street = models.CharField('logradouro', max_length=100)
    house_number = models.CharField('número', max_length=6)
    complement = models.CharField('complemento', max_length=100, null=True, blank=True)
    district = models.CharField('bairro', max_length=100)
    city = models.CharField('cidade', max_length=100)
    state = models.CharField('estado', max_length=100)

    def __str__(self):
        return self.CEP


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
        return str(self.school) + " " + self.name


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
    cpf = models.CharField('CPF', max_length=11, primary_key=True)
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


class Matriculation(models.Model):
    number_matriculation = models.IntegerField('matricula', default=random_string, primary_key=True)
    STATUS = (
        ('Ativo', 'Ativo'),
        ('Desativado', 'Desativado'),
        ('Em Curso', 'Em Curso'),
        ('Concluido', 'Concluido'),
    )
    status = models.CharField('situação', max_length=10, choices=STATUS, null=True)
    score = models.ForeignKey(Score, verbose_name="nota", null=True, blank=True)
    attendance = models.ForeignKey(Attendance, verbose_name="frequência", null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True, null=True)

    def __str__(self):
        return str(self.number_matriculation)

 
class ReportCard(models.Model):
    pass


class Student(CommonInfo):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='usuario')
    contact = models.ForeignKey(Contact, verbose_name="contato", default=False)
    address = models.ForeignKey(Address, verbose_name="endereço", default=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'alunos'
        verbose_name = 'aluno'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Employee(CommonInfo):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #funcionario tem matricula?
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
        return self.serie


class Class(models.Model):
    name = models.CharField('nome da turma', max_length=30)
    serie = models.ForeignKey(Serie, verbose_name="serie", null=True)
    academic_year = models.IntegerField('ano letivo', default=date.today().year)
    vacancies = models.CharField('vagas', max_length=10, default=0)
    unit = models.ForeignKey(Unit, verbose_name='unidade escolar', null=True)
    #financeiro
    value_tuition_fee = models.DecimalField('mensalidade', max_digits=5, decimal_places=2)


class TuitionFee(models.Model):
    discount_tuition_fee = models.DecimalField('desconto na mensalidade', max_digits=5, decimal_places=2)
    reason_discount_tuition_fee = models.CharField('motivo do desconto', max_length=255)
    expiration_day = models.PositiveIntegerField('dia de vencimento')
    FREQUENCY_PAYMENT = (
        ('Mensal', 'Mensal'),
        ('Bimestral', 'Bimestral'),
        ('Trimestral', 'Trimestral'),
        ('Semestral', 'Semestral'),
        ('Anual', 'Anual'),
        )
    frequency_payment = models.CharField('frequencia de pagamento', max_length=30, choices=FREQUENCY_PAYMENT)


class Matriculation(models.Model):
    number_matriculation = models.IntegerField('matricula', default=random_string)
    school_class = models.ForeignKey(Class, verbose_name="turma", null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE,  verbose_name='aluno')
    STATUS = (
        ('Ativo', 'Ativo'),
        ('Desativado', 'Desativado'),
        ('Em Análise', 'Em Análise'),
        ('Em Curso', 'Em Curso'),
        ('Concluido', 'Concluido'),
    )
    status = models.CharField('situação', max_length=10, choices=STATUS, null=True)
    report_card = models.ForeignKey(ReportCard, verbose_name="boletim", null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True, null=True)
    #financeiro
    tuition_fee = models.ForeignKey(TuitionFee, verbose_name='mensalidade')

    def __str__(self):
        return str(self.number_matriculation)


class AdditionalCost(models.Model):
    name = models.CharField('nome do custo', max_length=50)
    valor = models.DecimalField('valor', max_digits=5, decimal_places=2)


class Payment(models.Model):
    STATUS_PAYMENT = (
        ('Aguardando', 'Aguardando'),
        ('Cancelado', 'Cancelado'),
        ('Pago', 'Pago')
        )
    status = models.CharField('status do pagamento', max_length=15, choices=STATUS_PAYMENT)


class Subject(models.Model):
    name = models.CharField('nome da disciplina', max_length=50)