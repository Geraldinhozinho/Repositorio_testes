from django.shortcuts import render
from .models import Curso
# Create your views here.


def index(request):
    return render(request, 'cursos/index.html')

def informatica(request):
    cursos = Curso.objects.all()
    contexto = {
        'curso': cursos
    }
    return render(request, 'cursos/informatica.html',contexto)


def alimentos(request):
    return render(request, 'cursos/alimentos.html')


def apicultura(request):
    return render(request, 'cursos/apicultura.html')