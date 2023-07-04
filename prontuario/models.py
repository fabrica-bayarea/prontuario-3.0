from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    cpf = models.IntegerField(unique=True, blank=False)
    nascimento = models.DateField( auto_now=False, auto_now_add=False)
    telefone = models.IntegerField()
    endereco = models.CharField( max_length=100)



class Prontuario(models.Model):
    data = models.DateField( auto_now=True, auto_now_add=False)
    diagnostico = models.TextField()
    patologia = models.TextField()
    medicacoes = models.TextField(blank=True)


class Medico(models.Model):
    nome = models.CharField(max_length=100)
    
