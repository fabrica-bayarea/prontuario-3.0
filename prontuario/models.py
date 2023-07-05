from django.db import models
# Create your models here.


class ProntuarioMedico(models.Model):

    date = models.DateField(auto_now=True,)
    time = models.TimeField(auto_now=True, )
    patologia = models.TextField(default=None)
    pessoa_id = models.ForeignKey(
        'Pessoa', on_delete=models.CASCADE, default=None)


class Medico(models.Model):
    name = models.CharField(default=None, max_length=50, null=True)


class Pessoa(models.Model):
    name = models.CharField(default=None, max_length=100)
    address = models.CharField(default=None, max_length=200, blank=False)
    cpf = models.BigIntegerField(
        default=None, unique=True, blank=False, null=False)
    phone = models.BigIntegerField(default=None, blank=False)
    email = models.EmailField(default=None, max_length=254)
    birthday = models.DateField(
        default=None, editable=True, auto_now=False, auto_now_add=False)
    blood_type = models.CharField(default=None, blank=False, max_length=3)
