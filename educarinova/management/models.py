from django.db import models


class School(models.Model):
    company_name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    number_inep = models.CharField(max_length=100)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.company_name


class CommonInfo(models.Model):
    name = models.CharField('nome', max_length=150)
    cpf = models.CharField('CPF', max_length=11)
    date_of_birth = models.DateField()
    race = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    dispatch_entity_rg = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    naturalness = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Functionary(CommonInfo):
    pass


class Student(CommonInfo):
    matriculation = models.CharField(max_length=100)
    status = models.BooleanField()
    school = models.CharField(max_length=100)
    email = models.EmailField('e-mail')
    cell_phone = models.CharField('celular', max_length=20)
    phone = models.CharField('telefone', max_length=20)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    def __str__(self):
        return self.name

class Teacher(Functionary):
    pass


class Matriculation(models.Model):
    pass
