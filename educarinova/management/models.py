from django.db import models
from django.contrib.auth.models import User


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
    CEP = models.CharField('CEP', max_length=9)
    type_of_street = models.CharField('tipo de logradouro', max_length=100)
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
        return str(self.school) +" "+ self.name


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


class Student(CommonInfo):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matriculation = models.CharField('matrícula', max_length=100, primary_key=True)
    STATUS = (
        ('Ativo', 'Ativo'),
        ('Desativado', 'Desativado'),
        ('Em Curso', 'Em Curso'),
        ('Concluido', 'Concluido'),
    )
    status = models.CharField('situação', max_length=10, choices=STATUS)
    unit = models.ForeignKey(Unit, verbose_name="unidade", default=False)
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


class Matriculation(models.Model):
    pass
