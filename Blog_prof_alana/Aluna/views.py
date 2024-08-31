from django.shortcuts import render
from .models import Aluno, Sobre, Amigo,Convidados, Casamento
# Create your views here.
def index(request):
    dados = Aluno.objects.all() # Select do django
    contexto = {
        'lista': dados
    }
    return render(request, 'alunas/index.html',contexto)


def sobre(request):
    dados = Sobre.objects.all() # Select do django
    contexto = {
        'lista2': dados
    }
    return render(request, 'alunas/sobre.html',contexto)


def amigo(request):
    dados = Amigo.objects.all() # Select do django
    contexto = {
        'lista3': dados
    }
    return render(request, 'alunas/amigos.html',contexto)

def casamento(request):
    dados = Casamento.objects.all() # Select do django
    convite = Convidados.objects.all()
    contexto = {
        'lista4': dados,
        'lista5': convite
    }
    return render(request, 'alunas/casamento.html',contexto)
