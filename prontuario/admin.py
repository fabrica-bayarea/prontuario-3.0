from django.contrib import admin
from prontuario import models
# Register your models here.


@admin.register(models.ProntuarioMedico)
class ProntuarioMedico(admin.ModelAdmin):
    list_display = 'id', 'pessoa_id',


@admin.register(models.Medico)
class Medico(admin.ModelAdmin):
    list_display = 'id', 'name',
    ordering = '-id',


@admin.register(models.Pessoa)
class Pessoa(admin.ModelAdmin):
    list_display = 'id', 'name', 'cpf',
    ordering = '-id',
    # list_filter = 'created_date',
    search_fields = 'id', 'name',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'name',
    list_display_links = 'id',
