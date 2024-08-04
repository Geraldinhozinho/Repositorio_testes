from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'cursos/index.html')

def informatica(request):
    return render(request, 'cursos/informatica.html')


def alimentos(request):
    return render(request, 'cursos/alimentos.html')


def apicultura(request):
    return render(request, 'cursos/apicultura.html')