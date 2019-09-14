from django.contrib import admin
from core.models import Evento, Contato


# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento')

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    list_filter = ('usuario', 'empresa')


admin.site.register(Evento, EventoAdmin)


admin.site.register(Contato, ContatoAdmin)

