from django.shortcuts import render, redirect
from core.models import Evento, Contato

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):
#    evento = Evento.objects.get(id=1)
    evento = Evento.objects.all()
#    usuario = request.user
#    evento = Evento.objects.filter(usuario = usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

def lista_contatos(request):
    contato = Contato.objects.all()
    contatos = {'contatos':contato}
    return render(request, 'contato.html', contatos)