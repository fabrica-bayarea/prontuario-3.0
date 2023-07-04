from django.db import models
# Create your models here.


class ProntuarioMedico(models.Model):
    ...


class Medico(models.Model):
    ...


class Pessoa(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    cpf = models.IntegerField(unique=True, blank=False, null=False)
