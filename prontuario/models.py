from django.db import models
# Create your models here.


class Pessoa(models.Model):

    nome = models.CharField(
        max_length=200,
        default=None,
        blank=False,
    )
    data_nascimento = models.DateField(
        default=None,
        blank=False,
        unique=True,
    )
    cpf = models.BigIntegerField(
        max_length=11,
        blank=False,
        editable=False,
        unique=True,
        default=None
    )
    telefone = models.CharField(
        max_length=14,
        editable=True,
        unique=False,
        blank=False,
        default=None
    )
    email = models.EmailField(
        max_length=254,
        unique=False,
        editable=True,
        blank=False,
        default=None
    )
    tipo_sanguineo = models.CharField(
        max_length=3,
        editable=True,
        unique=True,
        default=None,
    )
    cep = models.BigIntegerField(
        unique=False,
        editable=True,
        blank=False,
        max_length=8,
        default=None,
    )
    endereco = models.CharField(
        max_length=200,
        unique=False,
        editable=True,
        blank=False,
        default=None,
    )


class Medico(models.Model):
    nome = models.CharField(
        unique=True,
        editable=True,
        blank=False,
        max_length=100,
        default=None,
    )
    especialidade = models.CharField(
        max_length=100,
        default=None,
        editable=True,
        unique=True,
        blank=False,
    )


class ProntuarioMedico(models.Model):
    data = models.DateTimeField(
        auto_now=True,
        unique=True,
    )
    queixa = models.TextField(
        blank=False,
        editable=True,
    )
