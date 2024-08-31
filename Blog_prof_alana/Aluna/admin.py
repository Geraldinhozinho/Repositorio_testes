from django.contrib import admin
from .models import Aluno, Sobre, Amigo, Casamento, Convidados
# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['data', 'titulo', 'descricao'] 
    

@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ['data_nascimento', 'titulo', 'descricao'] 
    
    
@admin.register(Amigo)
class AmigoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao'] 
    

@admin.register(Convidados)
class ConvidadosAdmin(admin.ModelAdmin):
    list_display = ['nome']
    
@admin.register(Casamento)
class CasamentoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'data','hora', 'local'] 