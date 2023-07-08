from django.contrib import admin
from prontuario import models
# Register your models here.


@admin.register(models.Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = "id", 'Nome',
    search_fields = 'Nome',
    ordering = '-Nome',


@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'especialidade',
    search_fields = 'nome', 'especialidade',
    ordering = '-nome',


@admin.register(models.ProntuarioMedico)
class ProntuarioMedicoAdmin(admin.ModelAdmin):
    list_display = 'id', 'data', 'queixa', 'exames', 'diagnostico', 'tratamento'
    search_fields = 'data',
    ordering = '-data',
