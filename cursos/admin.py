from django.contrib import admin
from .models import Curso
# Register your models here.

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'matricula')
    search_fields = ('nome', 'idade', 'matricula')
    list_filter = ('nome', 'idade', 'matricula')
    