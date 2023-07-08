from django.db import models
# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(
        name='Nome',
        max_length=200,
        default=None,
        blank=False,
    )
    data_nascimento = models.DateField(
        name='Data de Nascimento',
        default=None,
        blank=False,
        unique=True,
    )
    cpf = models.BigIntegerField(
        name='CPF',
        max_length=11,
        blank=False,
        editable=True,
        unique=True,
        default=None
    )
    telefone = models.CharField(
        name='Telefone',
        max_length=14,
        editable=True,
        unique=False,
        blank=False,
        default=None
    )
    email = models.EmailField(
        name='Email',
        max_length=254,
        unique=False,
        editable=True,
        blank=False,
        default=None
    )
    tipo_sanguineo = models.CharField(
        name='Tipo sanguineo',
        max_length=3,
        editable=True,
        unique=True,
        default=None,
    )
    cep = models.BigIntegerField(
        name='CEP',
        unique=False,
        editable=True,
        blank=False,
        max_length=8,
        default=None,
    )
    endereco = models.CharField(
        name='Endereço',
        max_length=200,
        unique=False,
        editable=True,
        blank=False,
        default=None,
    )
    atividade = models.BooleanField(
        name='Está ativo?',
        null=False,
        default=True,
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
    atividade = models.BooleanField(
        name='Esta ativo?',
        null=False,
        default=True
    )


class ProntuarioMedico(models.Model):
    pessoa = models.ForeignKey(
        Pessoa,
        verbose_name="Paciente",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    medico = models.ForeignKey(
        Medico,
        verbose_name="Medico",
        on_delete=models.SET_NULL,
        null=True
    )
    data = models.DateTimeField(
        auto_now=True,
        unique=True,
    )
    queixa = models.TextField(
        blank=False,
        editable=True,
    )
    exames = models.TextField(
        blank=False,
        editable=True,
    )
    diagnostico = models.TextField(
        blank=True,
        editable=True,
        unique=True,
    )
    tratamento = models.TextField(
        blank=True,
        editable=True,
        unique=True,
    )
