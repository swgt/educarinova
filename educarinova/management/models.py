from django.db import models


class School(models.Model):
    pass


class CommonInfo(models.Model):
    name = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)

    class Meta:
        abstract = True


class Functionary(CommonInfo):
    pass


class Student(CommonInfo):
    pass


class Teacher(Functionary):
    pass


class Matriculation(models.Model):
    pass
