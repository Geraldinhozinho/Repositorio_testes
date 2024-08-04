from django.urls import path
from cursos.views import index, informatica, alimentos, apicultura

urlpatterns = [
    path('',index,name='index'),
    path('index/',index,name='index'),
    path('informatica/',informatica,name='informatica'),
    path('alimentos/',alimentos,name='alimentos'),
    path('apicultura/',apicultura,name='apicultura'),
]